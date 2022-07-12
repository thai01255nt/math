import datetime
import json
import math
import re
from urllib.parse import quote_plus

import pandas as pd
import requests as requests


class YahooService:
    def __init__(self):
        self.headers = {
            "accept": "*/*",
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.53',
        }
        self.cookies = None
        self.crumb = None
        self.create_crumb()

    def create_crumb(self):
        res = requests.get("https://finance.yahoo.com", headers={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent': self.headers["user-agent"],
        })
        content = res.content.decode()
        search = """"user\":{\"crumb\":"""
        self.crumb = content[re.search(search, content).regs[0][0] + len(search):].split(",")[0][1:-1]
        self.crumb = quote_plus(self.crumb)
        self.cookies = dict(res.cookies)
        return

    def get_list_stock(self, limit: int, offset: int):
        params = {
            'crumb': self.crumb,
            'lang': "en-US",
            'region': "US",
            "formatted": 'true',
            "corsDomain": "finance.yahoo.com",
        }

        payload = {
            "size": limit,
            "offset": offset,
            "sortField": "intradaymarketcap",
            "sortType": "DESC",
            "quoteType": "EQUITY",
            "topOperator": "AND",
            "query": {
                "operator": "AND",
                "operands": [
                    {
                        "operator": "or",
                        "operands": [{"operator": "EQ", "operands": ["region", "us"]}]
                    }
                ]
            },
            "userId": "",
            "userIdType": "guid"
        }
        return json.loads(
            requests.post(
                'https://query1.finance.yahoo.com/v1/finance/screener',
                params=params,
                headers=self.headers,
                json=payload,
                cookies=self.cookies
            ).content.decode()
        )

    def get_historical(self, ticker: str, period1: datetime.datetime, period2: datetime.datetime):
        data = pd.read_csv(
            f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}'
            f'?period1={str(period1.timestamp())[:-2]}'
            f'&period2={str(period2.timestamp())[:-2]}'
            f'&interval=1d'
            f'&events=history'
            f'&includeAdjustedClose=true'
        )
        data = data.rename(columns={
            "Date": "date",
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Adj Close": "adjClose",
            "Volume": "volume",
        })
        data["date"] = pd.to_datetime(data["date"])
        return data
