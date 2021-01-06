from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticker, name="ticker"),
    path('2', views.interval_data, name="intraday_data"),
]
