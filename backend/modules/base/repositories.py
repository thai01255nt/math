from typing import List, TypeVar, Generic, Dict

from sqlalchemy.dialects.sqlite import insert

from backend.modules.base.entities import Base
from backend.db.sqlite_connector import session_scope

T = TypeVar("T")


class BaseRepo(Generic[T]):
    entity = None

    @classmethod
    def insert(cls, record: Base) -> T:
        with session_scope() as session:
            session.add(record)
        return record

    @classmethod
    def insert_many(cls, records: List[Base]) -> List[T]:
        with session_scope() as session:
            session.add_all(records)
        return records

    @classmethod
    def insert_many_on_conflict_do_not(cls, data: List[Dict]):
        with session_scope() as session:
            sql = insert(cls.entity).values(data).on_conflict_do_nothing()
            session.execute(sql)
        return

    @classmethod
    def get_by_id(cls, id: int) -> T:
        with session_scope() as session:
            record = session.query(cls.entity).filter(cls.entity.id == id).all()
        if len(record) == 0:
            return None
        return record[0]

    @classmethod
    def get_all(cls) -> List[T]:
        with session_scope() as session:
            return session.query(cls.entity).where(cls.entity.deletedAt.is_(None)).all()
