from flask_restful import Resource
import pymongo
import random
from faker import Faker

connection = pymongo.MongoClient('localhost', 27017)

database = connection['myPropertyDB']

collection = database['property_01']

data_list = []


class FakeData(Resource):
    def post(self):
        feed = [11, 12, 16]
        fake = Faker()

        for i in range(0, 300):
            data = {
                'id': i,
                'feed': random.choice(feed),
                'property_name': fake.name(),
                'price': random.randint(1000, 10000)
            }

            collection.insert(data)

        return {"response": "Successfully Added."}
