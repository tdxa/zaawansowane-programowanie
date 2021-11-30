import csv
from typing import List

from src.models.Movie import Movie
from src.models.Rating import Rating
from src.models.Tag import Tag


def get_movies_data() -> list[list[str]]:
    movies = []
    with open('data/movies.csv', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            movies.append(row)
    return movies


def get_serialized_movies():
    return [Movie(movie[0], movie[1], movie[2]).__dict__ for movie in get_movies_data()]


def get_ratings_data() -> list[list[str]]:
    ratings = []
    with open('data/ratings.csv', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            ratings.append(row)
    return ratings[1:]


def get_serialized_ratings():
    return [Rating(int(rating[0]), int(rating[1]), float(rating[2]), int(rating[3])).__dict__ for rating in
            get_ratings_data()]


def get_tags_data() -> list[list[str]]:
    tags = []
    with open('../data/tags.csv', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            tags.append(row)
    return tags[1:]


def get_serialized_tags():
    return [Tag(int(tag[0]), int(tag[1]), str(tag[2]), int(tag[3])).__dict__ for tag in
            get_tags_data()]
