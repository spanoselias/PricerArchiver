import datetime
import traceback

from StocksPricesRetriever import StockPricesDAO, DBUtils


# https://financialmodelingprep.com/developer/docs/#Stock-Price
# https://api.iextrading.com/1.0/ref-data/symbols
# https://www.alphavantage.co/documentation/
# https://github.com/wilsonfreitas/awesome-quant#data-sources

# dic = StockPricesDAO.getSymbols()
#
# for v in dic['symbolsList']:
#     symbol = v['symbol']
#     symbolName = v['name']
#     price = v['price']
#     print('Symbol:' + symbol + ' ' + 'SymbolName:' + symbolName + ' ' + 'Price:' + str(price))
#     StockPricesDAO.addSymbol(symbol, symbolName, price)

def retrieveAndAddCurrentStockPrices(pricesSchema):
    print('retrieveAndAddCurrentStockPrices is running...')
    reps = 0
    while (True):
        try:
            conn = DBUtils.getPostgresConnection()

            dic = StockPricesDAO.getSymbolsPrices()
            for v in dic['stockList']:
                StockPricesDAO.addSymbolPrice(conn, pricesSchema, v['symbol'], v['price'], datetime.datetime.utcnow())
            reps = reps + 1
            print('Run:' + str(reps))

        except:
            print(traceback.print_exc())
            conn.close()

# retrieveAndAddCurrentStockPrices('pricesarchiver')