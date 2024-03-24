import requests
import json

#essa realmente é minha api_key e ela é gratuita, portanto resolvi deixar aqui
# do contrário, não seria uma boa prática
api_key = "bfb07128-7be6-4ac6-84b1-973e0a098892"

#aqui é como a api da Coinmarket Cap tem que ser chamada para que funcione.
headers = {"X-CMC_PRO_API_KEY": api_key}

#url para receber os dados da api
base_url = "https://pro-api.coinmarketcap.com"

#parte da url que irá mudar de acordo com nosso objetivo
global_url = base_url + "/v1/cryptocurrency/listings/latest"

request = requests.get(global_url, headers=headers)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

#como quero informações chave de cada moeda e não ver tudo como na linha
# logo acima.

data = results["data"]
for currency in data:
    name = currency["name"]

#até tentei abrasileirar algumas coisas, como symbol pra sigla
# mas isso acabava só me confundindo na hora de escrever o código
    sigla = currency["symbol"]
    price = round(currency["quote"]["USD"]["price"], 2)
    percent_dif_24h = round(currency["quote"]["USD"]["percent_change_24h"],2)
    market_cap = round(currency["quote"]["USD"]["market_cap"], 2)

    price = ("U$D " + "{:,}".format(price))
    market_cap = ("U$D " + "{:,}".format(market_cap))
    percent_dif_24h = ("{:,}".format(percent_dif_24h))

    print(f"{name} ({sigla})")
    print(f"Price: {price}")
    print(f"24h change: {percent_dif_24h}%")
    print(f"Market Cap: {market_cap}")
    print()
