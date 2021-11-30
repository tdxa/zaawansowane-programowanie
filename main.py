from flask import Flask
from flask_restful import Resource, Api
from src.services.utlis import get_serialized_movies, get_serialized_ratings, get_serialized_links, get_serialized_tags

app = Flask(__name__)
api = Api(app)


class MoviesFromCsv(Resource):
    def get(self):
        return get_serialized_movies()


class RatingsFromCsv(Resource):
    def get(self):
        return get_serialized_ratings()


class LinksFromCsv(Resource):
    def get(self):
        return get_serialized_links()


class TagsFromCsv(Resource):
    def get(self):
        return get_serialized_tags()


api.add_resource(MoviesFromCsv, "/movies")
api.add_resource(RatingsFromCsv, "/ratings")
api.add_resource(LinksFromCsv, "/links")
api.add_resource(TagsFromCsv, "/tags")

if __name__ == '__main__':
    app.run(debug=True)
