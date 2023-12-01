"""
Resource: Brevets
"""
import flask
from flask import Response, current_app as app, request
from flask_restful import Resource

# You need to implement this in database/models.py
from database.models import Brevet as BrevetModel

class Brevets(Resource):
    def get(self):
        return Response(
            BrevetModel.objects().to_json(),
            mimetype='application/json',
            status=200
        )

    def post(self):
        # I'm too lazy to update/change all the key names, so here's a translation layer
        # for key names between the front-end and the api service.
        form_data = flask.json.loads(request.get_data())
        checkpoints = []
        for checkpoint in form_data['worksheet']:
            checkpoints.append({
                'distance': checkpoint['km'],
                'location': checkpoint['loc'],
                'open_time': checkpoint['open'].replace('T', ' '),
                'close_time': checkpoint['close'].replace('T', ' '),
            })
        brevet_dict = {
                'length': form_data['brevet_dist'],
                'start_time': form_data['start_time'].replace('T', ' '),
                'checkpoints': checkpoints
        }
        brevet = BrevetModel(**brevet_dict)
        return Response(
            brevet.save().to_json(),
            mimetype="application/json",
            status=200
        )

# MongoEngine queries:
# Brevet.objects() : similar to find_all. Returns a MongoEngine query
# Brevet(...).save() : creates new brevet
# Brevet.objects.get(id=...) : similar to find_one

# Two options when returning responses:
#
# return Response(json_object, mimetype="application/json", status=200)
# return python_dict, 200
#
# Why would you need both?
# Flask-RESTful's default behavior:
# Return python dictionary and status code,
# it will serialize the dictionary as a JSON.
#
# MongoEngine's objects() has a .to_json() but not a .to_dict(),
# So when you're returning a brevet / brevets, you need to convert
# it from a MongoEngine query object to a JSON and send back the JSON
# directly instead of letting Flask-RESTful attempt to convert it to a
# JSON for you.
