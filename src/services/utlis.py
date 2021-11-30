import csv
from typing import List

from src.models.Movie import Movie
from src.models.Rating import Rating


def get_movies_data() -> list[str]:
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
    with open('../data/ratings.csv', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            ratings.append(row)
    return ratings[1:]


def get_serialized_ratings():
    return [Rating(int(rating[0]), int(rating[1]), float(rating[2]), int(rating[3])).__dict__ for rating in
            get_ratings_data()]


print(get_serialized_ratings())
