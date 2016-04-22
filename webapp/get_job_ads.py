import platsannonser

def search(query):

	all_ads = list()

	all_ads = all_ads + platsannonser.search(query)

	return all_ads