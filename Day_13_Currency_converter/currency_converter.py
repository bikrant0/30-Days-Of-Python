# Currency Converter
from dotenv import load_dotenv
import requests, os

load_dotenv()

API_KEY = os.getenv("API_KEY")
currency = "USD"
def currency_converter():
    print("Currency Converter ")
    
    try:
        currency = str(input("Enter the currency: ").upper())
        amount = float(input("Enter the amount: "))
        target_currency = str(input("Tell me which currency you want to convert it: ").upper())

        r = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{currency}')
        data = r.json()
        if not currency in data['conversion_rates']:
            print(f"{currency} is not a valid currency code.")
            return
    except ValueError:
        print("Please enter the amount only. in interger.")
        return
    except ConnectionError:
        print("Is your internet working fine?. Please Check it and Try again. ")
        return
    except TypeError:
        print("Please enter valid input. ")
        return
    
    if target_currency in data["conversion_rates"]:
        rate = data['conversion_rates'][target_currency]
        print(amount*rate)
    else: 
        print("The currency you typed is not in the dictionary.")



currency_converter()