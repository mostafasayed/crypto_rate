from django.conf import settings
from celery import shared_task
from .models import Rate
import requests


@shared_task()
def fetch_exchange_rate(from_currency, to_currency):
    """
    Function to fetch exchange rate using alphavantage API
        Parameters:
            from_currency (string): the currency (or crypto) that we need it rate
            to_currency (string): the targed currenct (or crypto)
        Function stores results in DB as following:
        From Currency Code, To Currency Code, Exchange Rate, Bid Price, Ask Price, Rate Time
    """
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=%s&to_currency=%s&apikey=%s' % (
        from_currency, to_currency, settings.API_KEY)
    r = requests.get(url)
    data = r.json()
    realtime_rate = data['Realtime Currency Exchange Rate']
    Rate.objects.create(from_currency_code=realtime_rate['1. From_Currency Code'], to_currency_code=realtime_rate['3. To_Currency Code'],
                        exchange_rate=realtime_rate['5. Exchange Rate'], bid_price=realtime_rate[
                            '8. Bid Price'], ask_price=realtime_rate['9. Ask Price'],
                        rate_time=realtime_rate['6. Last Refreshed'])
