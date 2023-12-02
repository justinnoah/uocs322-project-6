"""
Resource: Brevet
"""
import flask
from flask import Response, request
from flask_restful import Resource

# You need to implement this in database/models.py
from database.models import Brevet as BrevetModel

class Brevet(Resource):
    def get(self, id):
        # Return the brevet with the given id or report the issue
        return Response(
            BrevetModel.objects().find_one(id=id).to_json(),
            mimetype="application/json",
            status=200
        )

    def delete(self, id):
        # Delete the brevet with id
        BrevetModel.objects().find_one(id=id).delete()
        return "", 200

    def put(self, id):
        bdict = flask.json.loads(request.get_data())
        BrevetModel.objects().find_one(id=id).update_one(upsert=True, **bdict)
        return "", 200
