import requests
import json

api_key = "bfb07128-7be6-4ac6-84b1-973e0a098892"

#aqui é como a api da Coinmarket Cap tem que ser chamada para que funcione.
headers = {"X-CMC_PRO_API_KEY": api_key}

#url para receber os dados da api
base_url = "https://pro-api.coinmarketcap.com"

global_url = base_url + "/v1/global-metrics/quotes/latest"

request = requests.get(global_url, headers=headers)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))

data = results["data"]

btc_dominance = round(data["btc_dominance"],2)
btc_dominance_var24h = round(data["btc_dominance_24h_percentage_change"],2)
eth_dominance = round(data["eth_dominance"],2)
total_marketcap = round(data["quote"]["USD"]["total_market_cap"],2)

total_marketcap = ("U$D " + "{:,}".format(total_marketcap))

print(btc_dominance)
print(total_marketcap)
