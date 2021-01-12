import psycopg2
from pycoingecko import CoinGeckoAPI
import schedule
import datetime
import time


class TickerScheduler():
    
    def ticker_trigger(self):
        cg = CoinGeckoAPI()
        content = cg.get_price(ids=['bitcoin', 'ripple', 'ethereum'], vs_currencies=["php","usd","eur"])
        return content

    def ticker_timer(self):
        print('Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
    
schedule.every(5).seconds.do(TickerScheduler.ticker_trigger)

while True:
    schedule.run_pending()
    time.sleep(1)
