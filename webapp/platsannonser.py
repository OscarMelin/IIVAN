import requests
import json


url = "http://api.arbetsformedlingen.se/af/v0/platsannonser/version"
headers = {"Accept-Language": "sv"}
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(url, headers = headers)
