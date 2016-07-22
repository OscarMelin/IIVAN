import requests
import json

from webapp import Job_ad

#http://api.arbetsformedlingen.se/af/v0/platsannonser/matchning?nyckelord=kock

def search(query):

	all_ads = list()

	url = "http://api.arbetsformedlingen.se/af/v0/platsannonser/matchning"
	headers = {"Accept-Language": "sv"}
	payload = {'nyckelord': query}
	response = requests.get(url, headers = headers, params = payload).text

	ads = json.loads(response)["matchningslista"]["matchningdata"]

	for ad in ads:
		all_ads.append(Job_ad.Job_ad(     \
			ad["annonsrubrik"],    \
			ad["yrkesbenamning"],  \
			ad["arbetsplatsnamn"], \
			ad["kommunnamn"],      \
			ad["annonsurl"]       \
			))
	
	return all_ads
