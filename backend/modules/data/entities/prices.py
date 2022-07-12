from sqlalchemy import text

from backend.common.consts import CommonConsts
from backend.modules.base.entities import Base
import sqlalchemy


class Price(Base):
    __tablename__ = 'prices'
    __table_args__ = (
        sqlalchemy.UniqueConstraint(
            "date",
            "symbol",
        ),
    )
    id = sqlalchemy.Column(
        sqlalchemy.BIGINT().with_variant(sqlalchemy.Integer, "sqlite"), primary_key=True, nullable=False
    )
    date = sqlalchemy.Column(sqlalchemy.DATETIME, nullable=False)
    symbol = sqlalchemy.Column(sqlalchemy.TEXT, nullable=False)
    open = sqlalchemy.Column(sqlalchemy.TEXT)
    high = sqlalchemy.Column(sqlalchemy.TEXT)
    low = sqlalchemy.Column(sqlalchemy.TEXT)
    close = sqlalchemy.Column(sqlalchemy.TEXT)
    adjClose = sqlalchemy.Column(sqlalchemy.TEXT)
    volume = sqlalchemy.Column(sqlalchemy.TEXT)
    createdAt = sqlalchemy.Column(
        sqlalchemy.TEXT, nullable=False, default=text(f"strftime('{CommonConsts.TIME_FORMAT}')")
    )
    updatedAt = sqlalchemy.Column(
        sqlalchemy.TEXT,
        nullable=False,
        default=text(f"strftime('{CommonConsts.TIME_FORMAT}')"),
        onupdate=text(f"strftime('{CommonConsts.TIME_FORMAT}')"),
    )
    deletedAt = sqlalchemy.Column(sqlalchemy.TEXT, default=None)
