from sqlalchemy import text

from backend.common.consts import CommonConsts
from backend.modules.base.entities import Base
import sqlalchemy


class Stock(Base):
    __tablename__ = 'stocks'
    __table_args__ = (
        sqlalchemy.UniqueConstraint(
            "symbol",
            "exchange",
            "shortName",
            "fullExchangeName",
            "displayName",
            "quoteType",
            "longName",
        ),
    )
    symbol = sqlalchemy.Column(sqlalchemy.TEXT, nullable=False, primary_key=True)
    exchange = sqlalchemy.Column(sqlalchemy.TEXT, nullable=False)
    shortName = sqlalchemy.Column(sqlalchemy.TEXT)
    fullExchangeName = sqlalchemy.Column(sqlalchemy.TEXT)
    displayName = sqlalchemy.Column(sqlalchemy.TEXT)
    quoteType = sqlalchemy.Column(sqlalchemy.TEXT, nullable=False)
    longName = sqlalchemy.Column(sqlalchemy.TEXT)
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


CONSTRAINT = """
(
case when symbol is not null then symbol else '' end,
case when exchange is not null then exchange else '' end,
case when shortName is not null then shortName else '' end,
case when fullExchangeName is not null then fullExchangeName else '' end,
case when displayName is not null then displayName else '' end,
case when quoteType is not null then quoteType else '' end,
case when longName is not null then longName else '' end
);
"""
CONSTRAINT_STOCK = text(
    f"""
    CREATE UNIQUE INDEX IF NOT EXISTS {Stock.__tablename__}AllColumnIndex
    ON {Stock.__tablename__}
    {CONSTRAINT}
    """
)
