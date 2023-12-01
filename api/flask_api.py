"""
Brevets RESTful API
"""
import logging
import os

from flask import Flask
from flask_restful import Api
from mongoengine import connect

from resources.brevet import Brevet
from resources.brevets import Brevets

# Connect MongoEngine to mongodb
connect(host=f"mongodb://{os.environ['MONGODB_HOSTNAME']}:27017/brevetsdb")

CONFIG = {
    'PORT': int(os.environ['PORT']),
    'DEBUG': bool(os.environ['DEBUG']),
    'DBHOST': os.environ['MONGODB_HOSTNAME'],
}

# Start Flask app and Api here:
app = Flask(__name__)
app.debug = CONFIG['DEBUG']
if app.debug:
    app.logger.setLevel(logging.DEBUG)
api = Api(app, prefix='/api')
api.add_resource(Brevet, '/brevet')
api.add_resource(Brevets, '/brevets')

# Bind resources to paths here:
# api.add_resource(...)

if __name__ == '__main__':
    # Run flask app normally
    # Read DEBUG and PORT from environment variables.
    app.run(port=CONFIG['PORT'], host='0.0.0.0')
