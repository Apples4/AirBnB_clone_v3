#!/usr/bin/python3
""" API test stats"""

from api.v1.views import *
from models import storage
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
