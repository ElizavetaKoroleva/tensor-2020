""" Билетная касса театра """
import os

from flask import Flask, jsonify
from flask_pymongo import PyMongo

from .encoder import MongoJSONEncoder

APP = Flask(__name__, static_folder="../client")
APP.json_encoder = MongoJSONEncoder
APP.config["JSON_AS_ASCII"] = False
APP.config["MONGO_URI"] = os.environ["MONGO_URI"]
MONGO = PyMongo(APP)

from . import data_bd

if os.environ.get("FLASK_ENV") == "development" and MONGO.db.event.count_documents({}) == 0:
    data_bd.add_event1()
    data_bd.add_event2()
    data_bd.add_event3()
    data_bd.add_mock_events(7)

from . import views
from .api import list_events, booking
