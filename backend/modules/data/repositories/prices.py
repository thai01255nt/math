import datetime
from typing import Optional

from backend.db import session_scope
from backend.modules.base.repositories import BaseRepo
from backend.modules.data.entities import Price


class PriceRepo(BaseRepo[Price]):
    entity = Price

    @classmethod
    def get_max_date_by_symbol(cls, symbol: str) -> Optional[datetime.datetime]:
        condition = ((Price.symbol == symbol) & (Price.deletedAt.is_(None)))
        with session_scope() as session:
            records = session.query(Price).where(condition).order_by(Price.date.desc()).limit(1).all()
            if len(records) == 0:
                return None
            return records[0].date
