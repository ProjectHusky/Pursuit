from flask import Flask
from flask import request
from flask import jsonify
from google_maps import Maps
from Yelp import Yelp
import spotipy
import spotify
from spotipy.oauth2 import SpotifyClientCredentials
app = Flask(__name__)
gmap = Maps()
yelp = Yelp()


client_credentials_manager = SpotifyClientCredentials(client_id="1b2cd56013a647308e007cb88a1f1d2c", client_secret="0b90798a8d2847938b977b428f0e210d")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


@app.route('/map', methods = ['GET'])
#.com/map?var1="112038"&var2="665"
def get_directions():
    a = request.args.get("var1")
    print(a)
    b = request.args.get("var2")
    print(b)
    raw = gmap.get_directions(a, b)
    print(type(raw))
    return jsonify(raw)

@app.route('/yelp')
def yelp_me():
    lon = request.args.get("longitude")
    print(lon)
    lat = request.args.get("latitude")
    print(lat)
    return jsonify(yelp.find_nearest(lon, lat))
    #return "Hello"


@app.route("/spotify", methods = ['GET'])
#.com/spotify?seed1="Led Zeppelin"&seed2="Red Velvet"&seed3="LiSa"&seed4="Frank Ocean"&seed="Migos"
def create_playlist():

    seeds = []
    seeds.append(request.args.get("seed1"))
    seeds.append(request.args.get("seed2"))
    seeds.append(request.args.get("seed3"))
    seeds.append(request.args.get("seed4"))
    seeds.append(request.args.get("seed5"))
    if '""' in seeds:
        seeds.remove('""')

    spotify_ids = []
    for seed in seeds:
        spotify_ids.append(spotify.get_artist_id(seed, sp))
    print(spotify_ids)

    return "What"

if __name__ == '__main__':
    app.run()
