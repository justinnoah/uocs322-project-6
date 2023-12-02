"""
Resource: Brevets
"""
import flask
from flask import Response, current_app as app, request
from flask_restful import Resource

# You need to implement this in database/models.py
from database.models import Brevet as BrevetModel

class Brevets(Resource):
    # Per instructions, get all of the stored brevets!
    def get(self):
        return Response(
            BrevetModel.objects().to_json(),
            mimetype='application/json',
            status=200
        )

    # Store a brevet!
    def post(self):
        # Instead of updating all the key names for the front/backends based on
        # the object model attributes, I created a "translation" layer
        try:
            # In a try block in case json parsing fails
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
            brevet = BrevetModel(**brevet_dict).save()
            # Return the jsonified brevet
            return Response(
                {'_id': str(brevet.id)},
                mimetype="application/json",
                status=200
            )
        except:
            raise
