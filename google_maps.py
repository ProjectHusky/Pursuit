import googlemaps
from datetime import datetime
import config



class Maps:
    def __init__(self):
        self.gmaps = googlemaps.Client(key=config.maps_key)


        # # Geocoding an address
        # geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
        #
        # # Look up an address with reverse geocoding
        # reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
        #
        # # Request directions via public transit
        # now = datetime.now()
        # directions_result = gmaps.directions("Sydney Town Hall",
        #                                      "Parramatta, NSW",
        #                                      mode="transit",
        #                                      departure_time=now)

    def get_directions(self, point_a, point_b):
        point_a_geocode = self.gmaps.geocode(point_a)
        point_b_geocode = self.gmaps.geocode(point_b)
        print(point_a_geocode)
        print(point_b_geocode)
        return self.gmaps.directions(origin=point_a_geocode, destination=point_b_geocode, mode="driving")






