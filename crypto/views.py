from django.shortcuts import render
from django.utils.timezone import make_aware
from datetime import datetime
import datetime
from pycoingecko import CoinGeckoAPI
from crypto.forms import CryptoDataForm

def ticker(request):
    cg = CoinGeckoAPI()
    content = cg.get_price(ids=['bitcoin', 'ripple', 'ethereum'], vs_currencies=["php","usd","eur"])
    return render(request, 'crypto/ticker.html', {'content':content})


def interval_data(request):
    cg = CoinGeckoAPI()
    content = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', from_timestamp='1609718400', to_timestamp='1609804800')
    
    categories = []
    date_time = []
    prices = []
    
    for key, values in content.items():
        for value in values:
            categories.append(key)
            date_time.append(str(value[0]))
            prices.append(round(value[1],2))
                             
            
    converted = [x[:-3] for x in date_time]
    time_and_date = [datetime.datetime.fromtimestamp(int(x)).strftime("%x %X") for x in converted]
    zip_content = [{a: {b: c}} for (a, b, c) in zip(categories, time_and_date, prices)]
    
        
    return render(request, 'crypto/historical.html', {'content':zip_content})
        
