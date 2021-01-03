from database import db
from flask.blueprints import Blueprint
from flask_restful import Api, Resource, url_for

index = Blueprint('index', __name__)
api = Api(index)

class Index(Resource):
    def get(self):
        return 'Welcome to WanCloud Server'


api.add_resource(Index, '/')
