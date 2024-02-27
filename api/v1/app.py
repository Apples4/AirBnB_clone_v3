#!/usr/bin/python3
""" app.py file """
import os
from models import storage
from flask import Flask
from api.v1.views import app_views

app = Flask(__name__)

host = os.environ.get('HBNB_API_HOST', 0.0.0.0)
port = os.environ.get('HBNB_API_PORT', 5000)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})



@app.teardown_appcontext
def closedb():
    '''function to close db'''
    return storage.close()

@app.errorhandler(404)
def pagerr(err):
    ''' function handles error '''
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host=host, port=int(port), threaded=True)
