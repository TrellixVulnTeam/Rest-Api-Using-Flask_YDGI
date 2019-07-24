from flask import Blueprint
from flask_restful import Api
from resources.hello import Hello
from resources.category import Category
from resources.fake import FakeData
from resources.pagination import Pagination


api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# Route
api.add_resource(Hello, '/hello')
api.add_resource(Category, '/category')
api.add_resource(FakeData, '/fake')
api.add_resource(Pagination, '/pagination')


















