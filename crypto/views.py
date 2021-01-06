from django.shortcuts import render
from django.utils.timezone import make_aware
from datetime import datetime
from pycoingecko import CoinGeckoAPI

def ticker(request):
    cg = CoinGeckoAPI()
    content = cg.get_price(ids=['bitcoin', 'ripple', 'ethereum'], vs_currencies=["php","usd","eur"])
    return render(request, 'crypto/ticker.html', {'content':content})


def interval_data(request):
    cg = CoinGeckoAPI()
    content = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', from_timestamp='1609718400', to_timestamp='1609804800')
    #for date_time, price in content['prices']:
        #date_time = make_aware(datetime.fromtimestamp(item))
    return render(request, 'crypto/historical.html', {'content':content})
    