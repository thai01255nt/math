from backend.modules.base.repositories import BaseRepo
from backend.modules.data.entities import Stock


class StockRepo(BaseRepo[Stock]):
    entity = Stock
