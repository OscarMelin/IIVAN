import requests
import json

#http://api.arbetsformedlingen.se/af/v0/platsannonser/matchning?nyckelord=kock

url = "http://api.arbetsformedlingen.se/af/v0/platsannonser/version"
headers = {"Accept-Language": "sv"}
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(url, headers = headers)


def search(query):

	url = "http://api.arbetsformedlingen.se/af/v0/platsannonser/matchning"
	headers = {"Accept-Language": "sv"}
	payload = {'nyckelord': query}
	response = requests.get(url, headers = headers, params = payload).text

	ads = json.loads(response)["matchningslista"]["matchningdata"]

	return ads
