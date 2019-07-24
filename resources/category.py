
from flask import request
from flask_restful import Resource

class Category(Resource):
    def get(self):
        categories = ({"id": 1, "name": "Hassan"}, {"id": 2, "name": "Zahid"})
        return {'status': 'success', 'data': categories}, 200

