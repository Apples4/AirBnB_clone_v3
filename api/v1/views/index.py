#!/usr/bin/python3
""" API test stats"""

from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    ''' displays status '''
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def stats():
    ''' displays number of object type '''

    return jsonify({"amenities": storage.count("Amenitiess"),
                    "cities": storage.count("Cities"),
                    "places": storage.count("Places"),
                    "reviews": storage.count("Reviews"),
                    "states": storage.count("States"),
                    "users": storage.count("Users")
                    })
