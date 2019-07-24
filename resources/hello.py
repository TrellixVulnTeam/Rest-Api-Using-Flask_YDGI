# Import necessary module
from flask import jsonify, request
from flask_restful import Resource
import pymongo

connection = pymongo.MongoClient('localhost', 27017)

# create Database
database = connection['myPropertyDB']
# Create Collection name
collection = database['property_01']

data_list = []


class Hello(Resource):
    def get(self):
        # count all data
        count = collection.count()

        for data in collection.find({'feed': 12}):
            data_list.append(str(data))
        return {'All Data = ': count, 'data': data_list}, 200

    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Error"}
            return jsonify(data)
        else:
            p_id = data.get('id')
            if p_id:
                if collection.find_one({"id": p_id}):
                    return {"response": "This data is  already exist."}
                else:
                    collection.insert_one(data)
            else:
                return {"response": "This id is missing."}

        return {"response": "Successfully Added data."}









