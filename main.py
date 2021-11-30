from flask import Flask
from flask_restful import Resource, Api
from src.services.utlis import get_serialized_movies

app = Flask(__name__)
api = Api(app)


class MoviesFromCsv(Resource):
    def get(self):
        return get_serialized_movies()


api.add_resource(MoviesFromCsv, "/")

app.run(host="0.0.0.0", port=5000, debug=True)
