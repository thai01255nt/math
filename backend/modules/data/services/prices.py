import datetime
import json
import math

from backend.common.consts import CommonConsts
from backend.db import session_scope
from backend.modules.data.entities import Price
from backend.modules.data.repositories import PriceRepo, StockRepo
from backend.modules.third_parties.yahoo import YahooService


class PriceService:
    def __init__(self):
        self.price_repo = PriceRepo
        self.stock_repo = StockRepo
        self.yahoo_service = YahooService()

    def crawl_prices(self):
        with session_scope() as session:
            stocks = self.stock_repo.get_all()
            for i in range(len(stocks)):
                stock = stocks[i]
                start_date = self.price_repo.get_max_date_by_symbol(symbol=stock.symbol)
                if start_date is None:
                    start_date = datetime.datetime(day=31, month=12, year=2000)
                start_date = start_date + datetime.timedelta(days=1)
                end_date = datetime.datetime.now().date()
                end_date = datetime.datetime(
                    day=end_date.day,
                    month=end_date.month,
                    year=end_date.year,
                )
                if end_date < start_date:
                    continue
                data = self.yahoo_service.get_historical(ticker=stock.symbol, period1=start_date, period2=end_date)
                data = data[data["date"] >= start_date]
                data["symbol"] = stock.symbol
                data = data.to_dict(orient="records")
                self.price_repo.insert_many(records=[Price(**data_item) for data_item in data])
                print(i, len(stocks), stock.symbol)
                session.commit()
        return
