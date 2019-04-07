import json #--- For return list

def init_data(query):
	import http.client
	conn = http.client.HTTPSConnection("api.bitcoincharts.com")
	conn.request("GET","{}".format(query))
	res = conn.getresponse()
	data = res.read()
	return json.loads(data.decode("utf-8"))

def process():
	data = init_data('/v1/weighted_prices.json')
	return data

def cal_coin(price):
	return (float(price) > 40)
	# if float(price) > 40:
	# 	return True
	# else:
	# 	return False

def process_market():
	data = init_data('/v1/markets.json')
	return data

def coins():
	import http.client
	conn = http.client.HTTPSConnection("api.coinmarketcap.com")
	conn.request("GET","/v1/ticker/")
	res = conn.getresponse()
	data = res.read()
	return json.loads(data.decode("utf-8"))

def process_coins():
	data = coins()
	al_coin = []
	for item in data:
		item["over40usd"] = cal_coin(item["price_usd"]) 
		al_coin.append(item)
	return al_coin