from google_maps import Maps

gmap = Maps()

point_a = "11203 81st st. ave s. Seattle WA, 98178"
point_b = "665 Taylor Ave NW Renton WA, 98057"

print (gmap.get_directions(point_a, point_b))