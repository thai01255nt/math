from backend.modules.data.services import StockService, PriceService

# a = StockService()
# a.crawl_stocks()

a = PriceService()
a.crawl_prices()
