import csv
from src.models.Movie import Movie


def get_movies_data():
    movies = []
    with open('data/movies.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            movies.append(row)
    return movies


def get_serialized_movies():
    # print(get_movies_data())
    return [Movie(movie[0], movie[1], movie[2]).__dict__ for movie in get_movies_data()]
