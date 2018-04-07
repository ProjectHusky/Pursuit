from google_maps import Maps
import pprint
gmap = Maps()

pp = pprint.PrettyPrinter(indent=2)
# point_a = "11203 81st st. ave s. Seattle WA, 98178"
# point_b = "665 Taylor Ave NW Renton WA, 98057"
point_a = "665 taylor ave nw renton wa 98057"
point_b = "New York City, New York"

pp.pprint (gmap.get_directions(point_a, point_b))