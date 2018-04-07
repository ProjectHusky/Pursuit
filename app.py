from flask import Flask
from flask import request
from google_maps import Maps
app = Flask(__name__)
gmap = Maps()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/map/')
def get_directions():
    point_a = request.args.get('point_a')
    point_b = request.args.get('point_b')

if __name__ == '__main__':
    app.run()
