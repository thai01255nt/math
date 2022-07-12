from backend.modules.base.entities import Base
from backend.modules.data.entities import *
from backend.db.sqlite_connector import engine, session_scope

Base.metadata.create_all(bind=engine)
with session_scope() as session:
    session.execute(CONSTRAINT_STOCK)
    session.commit()
