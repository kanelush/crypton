import requests
from coinpaprika import client as Coinpaprika


client = Coinpaprika.Client()

a = client.tickers()

def extras(request):
    responses = a
    response = requests.get('https://static.coinpaper.io/api/coins.json').json()
    context = { 
        'responses': responses,
        'response': response, 
                }
    return context
