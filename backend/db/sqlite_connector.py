import os
import threading
from contextlib import contextmanager
from typing import ContextManager

from flask import session as flask_session

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from sqlalchemy.pool import QueuePool

from backend.utils.logger import LOGGER

LOCAL_SESSION = {}
DNS = os.environ.get("SQLITE_DNS", None)
MIN_CONN = 2
MAX_CONN = 4
MAX_TIMEOUT = 60 * 60 * 24 * 2
engine = create_engine(
    DNS, poolclass=QueuePool, pool_pre_ping=True, pool_size=MAX_CONN - MIN_CONN, max_overflow=MIN_CONN
)
session = Session(bind=engine.connect())
session.execute(text('pragma foreign_keys=ON'))
session.commit()
session.close()
del session


def get_unique_thread_key():
    thread_id = threading.get_ident()
    process_id = os.getpid()
    unique_thread_key = str(process_id) + "-" + str(thread_id)
    return unique_thread_key


def set_session(session):
    try:
        flask_session["SQLITE_SESSION"] = session
    except:
        global LOCAL_SESSION
        if session is None:
            try:
                LOCAL_SESSION.pop(get_unique_thread_key())
            except:
                pass
        else:
            LOCAL_SESSION[get_unique_thread_key()] = session


def get_session():
    try:
        return flask_session["SQLITE_SESSION"]
    except:
        global LOCAL_SESSION
        return LOCAL_SESSION.get(get_unique_thread_key(), None)


@contextmanager
def session_scope() -> ContextManager[Session]:
    """
    Provide a transactional scope around a series of operations.
    Shouldn't keep session alive too long, it will block a connection of pool connections.
    """
    session: Session
    reuse_session = get_session()
    if reuse_session is None:
        session = Session(bind=engine.connect())
        set_session(session=session)
    else:
        session = reuse_session
    try:
        yield session
        if reuse_session is None:
            session.commit()
    except Exception as exception:
        LOGGER.error(exception, exc_info=True)
        if reuse_session is None:
            session.rollback()
        raise exception
    finally:
        if reuse_session is None:
            session.close()
            set_session(session=None)
