from django.shortcuts import render
from django.http import JsonResponse
from pycoingecko import CoinGeckoAPI

def ticker(request):
    cg = CoinGeckoAPI()
    context = cg.get_price(ids=['bitcoin', 'ripple', 'ethereum'], vs_currencies=["php","usd","eur"])
    return JsonResponse({'context':context})


def historical(request):
    cg = CoinGeckoAPI()
    id = request.POST.get('id')
    date_request = request.POST.get('date_request')
    
    