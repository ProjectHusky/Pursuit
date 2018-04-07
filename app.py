from flask import Flask
from flask import request
from flask import jsonify
from google_maps import Maps
from Yelp import Yelp
app = Flask(__name__)
gmap = Maps()
yelp = Yelp()

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

if __name__ == '__main__':
    app.run()
