import requests
from API_Key import key

def get_Conversion_rates():

    url = f'https://v6.exchangerate-api.com/v6/{key}/latest/USD'

    response = requests.get(url)
    data = response.json()
    rates = data["conversion_rates"]
    lst = list(rates.keys())

    return {
        "options": lst,
        "rates": rates
    }

get_Conversion_rates()