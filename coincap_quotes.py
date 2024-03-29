import requests
import json

api_key = "bfb07128-7be6-4ac6-84b1-973e0a098892"

#aqui é como a api da Coinmarket Cap tem que ser chamada para que funcione.
headers = {"X-CMC_PRO_API_KEY": api_key}

#url para receber os dados da api
base_url = "https://pro-api.coinmarketcap.com"

#input para filtrar e visualizar apenas uma moeda
symbol = input("Insira a sigla da moeda que deseja consultar: ").upper()
# symbol = symbol.upper()

#como só será visualizada uma moeda por vez, a documentação sugere que seja
#utilizado o quotes ao invés do listing, por questões de velocidade, porém
# as informações são as mesmas nos dois
global_url = base_url + "/v1/cryptocurrency/quotes/latest?" + "symbol=" + symbol

request = requests.get(global_url, headers=headers)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

#como o symbol ou sigla já foi filtrada no inicio, não há necessidade de buscar
#dentro de data
data = results["data"]
currency = data[symbol]
name = currency["name"]
price = round(currency["quote"]["USD"]["price"], 2)
percent_dif_24h = round(currency["quote"]["USD"]["percent_change_24h"],2)
market_cap = round(currency["quote"]["USD"]["market_cap"], 2)

price = ("U$D " + "{:,}".format(price))
market_cap = ("U$D " + "{:,}".format(market_cap))
percent_dif_24h = ("{:,}".format(percent_dif_24h))

print(f"{name} ({symbol})")
print(f"Price: {price}")
print(f"24h change: {percent_dif_24h}%")
print(f"Market Cap: {market_cap}")
print()
