import config
import requests
import pprint

class Yelp():

    def __init__(self):
        self.api_key = config.yelp_key


    def find_nearest(self, longitude, latitude):
        headers = {
            'Authorization': 'Bearer %s' % self.api_key,
        }

        url = "https://api.yelp.com/v3/businesses/search"

        url_params = {
            'term': "food",
            'longitude': longitude,
            'latitude': latitude,
            'radius': 1600,  # Meters
            'limit': 10,
            'sort_by': "rating"
        }
        response = requests.request('GET', url, headers=headers, params=url_params)
        #response = requests.get(req)
        data = response.json()
        print (data)
        #pprint.PrettyPrinter.pprint(data)
        return data
