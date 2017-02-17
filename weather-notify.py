# Yoseph Tesfagabe
# Pythong 2.7.12
# weather-notify.js

import requests
import json
import logging
import sys
import getopt
import collections
import datetime

def main(args):
	data = ''
	message = ''
	daysForecasted = 1
	# Load configurations from config.json
	file = open('config.json', 'r')
	config = json.load(file)
	file.close()
	url =  'http://api.openweathermap.org/data/2.5/forecast?id=4987064&units=metirc&APPID=' + str(config["owmApiKey"])
	data = getData(url)

	parsedData = parseData(data, daysForecasted)
	print parsedData

# call api and return results
def getData(url):
	r = requests.get(url)
	print(r.text)
	return r.text

# only keep the info I care about
def parseData(data, daysForecasted):
	cityName = data['city']['name']
	descriptions = collections.OrderedDict()
	uniqueDescriptions = set()
	temps = collections.OrderedDict()
	messageTemps = ''

	for listing in data['list']:
		temps[listing['dt']] = listing['main']['temp']
		descriptions[listing['dt']] = listing['weather'][0]['description']
		uniqueDescriptions.add(listing['weather'][0]['description'])

	loops = daysForecasted * 8

	for a, b in zip(descriptions, temps):
		if datetime.date.today() == datetime.date.fromtimestamp(a):
			print('true')
		messageTemps = messageTemps + datetime.datetime.fromtimestamp(a).strftime("%H") + ":" + str(int(temps[b])) + ", "

	return str(cityName) +  ": " + messageTemps

def notify(message):
	print("test")

main(sys.argv)