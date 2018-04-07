from flask import Flask
from flask import request
from flask import jsonify
from google_maps import Maps
app = Flask(__name__)
gmap = Maps()

@app.route('/')
def hello_world():
    return 'Hello World!'


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



if __name__ == '__main__':
    app.run()
