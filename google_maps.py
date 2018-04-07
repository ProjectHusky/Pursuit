import googlemaps
from datetime import datetime
import config
import pprint


class Maps:
    def __init__(self):
        self.gmaps = googlemaps.Client(key=config.maps_key)
        self.pp = pprint.PrettyPrinter(indent=2)

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
        # self.pp.pprint(point_a_geocode)
        # self.pp.pprint(point_b_geocode)
        return self.gmaps.directions(origin=point_a, destination=point_b, mode="driving")[0]["legs"]



    def standardize_time(self, time):
        tokens = time.split(" ")

        duration = 0
        for x in range(1, len(tokens), 2):
            unit = tokens[x]
            time_val = tokens[x - 1]
            if unit == "min" or unit == "mins":
                duration += float(tokens[x - 1])
            elif unit == "hours" or unit == "hour":
                duration += float(time_val) * 60
            elif unit == "day" or unit == "days":
                duration += float(time_val) * 60 * 24
            elif unit == "week" or unit == "weeks":
                duration += float(time_val) * 60 * 24 * 7

        return duration




