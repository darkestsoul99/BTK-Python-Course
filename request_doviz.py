import requests
import json 

api_url = 'https://api.exchangeratesapi.io/v1/latest?access_key=bueYe6KYXxmIUKDkcaX3G6ukC3QqslBG&base='

sold = input("Bozulan döviz türü")
bought = input("Alınan döviz türü")
amount = input("Ne kadar bozdurmak istiyorsunuz?")

result = requests.get(api_url+sold)
result = json.loads(result.text)

print(result)