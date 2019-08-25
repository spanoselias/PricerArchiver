import _thread

from StocksPricesRetriever import PricesRetriever, HistoricalPricesRetriever

print('Retriever is running...')

try:
    p1 = _thread.start_new_thread(PricesRetriever.retrieveAndAddCurrentStockPrices, ("pricesarchiver",))
    # p2 = _thread.start_new_thread(HistoricalPricesRetriever.retrieveAndAddHistoricalStockPrices,("pricesarchiver",))

except:
    print("Error: unable to start thread")

while 1:
    pass
