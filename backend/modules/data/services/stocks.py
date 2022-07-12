import json
import math

from backend.db import session_scope
from backend.modules.data.repositories import StockRepo
from backend.modules.third_parties.yahoo import YahooService


class StockService:
    def __init__(self):
        self.stock_repo = StockRepo
        self.yahoo_service = YahooService()

    def crawl_stocks(self):
        page_size = 100
        included_keys = [
            "symbol",
            "exchange",
            "shortName",
            "fullExchangeName",
            "displayName",
            "quoteType",
            "longName",
        ]
        data = self.yahoo_service.get_list_stock(limit=1, offset=0)
        page_count = math.ceil(data['finance']['result'][0]['total'] / page_size)
        with session_scope() as session:
            for page_current in range(page_count):
                list_data = []
                data = self.yahoo_service.get_list_stock(
                    limit=page_size,
                    offset=page_current * page_size
                )['finance']
                if data["error"] is not None:
                    if data["error"]["description"] == 'offset and size is over threshold':
                        break
                    else:
                        raise Exception(str(data))
                data = data['result'][0]['quotes']
                for data_item in data:
                    list_data.append({k: data_item[k] if k in data_item else None for k in included_keys})
                self.stock_repo.insert_many_on_conflict_do_not(data=list_data)
                print(f"offset: {page_size * page_current}")
                session.commit()
