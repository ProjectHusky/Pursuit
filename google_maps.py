import googlemaps
from datetime import datetime
import config

gmaps = googlemaps.Client(key=config.maps_key)

class Maps:
    def __init__(self, database):

        # Geocoding an address
        geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

        # Look up an address with reverse geocoding
        reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

        # Request directions via public transit
        now = datetime.now()
        directions_result = gmaps.directions("Sydney Town Hall",
                                             "Parramatta, NSW",
                                             mode="transit",
                                             departure_time=now)