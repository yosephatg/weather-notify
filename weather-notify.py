# Yoseph Tesfagaber
# Pythong 2.7.12
# weather-notify.js

import requests
import json
import logging
import sys
import getopt

def main(args):
	data = ''
	message = ''
	# Load configurations from config.json
	file = open('config.json', 'r')
	config = json.load(file)
	file.close()

	url = 'http://api.openweathermap.org/data/2.5/weather?id=4987064&APPID=' + str(config["owmApiKey"])
	data = getData(url)
	print(data)


def getData(url):
	# call api, save as json
	r = requests.get(url)
	print(r.encoding)
	print(r.text)
	return r.text

def parseData(data):
	print('test')

def notify(message):
	print("test")

main(sys.argv)