import csv

from src.models.Link import Link
from src.models.Movie import Movie
from src.models.Rating import Rating
from src.models.Tag import Tag


def get_movies_data():
    movies = []
    with open('src/data/movies.csv', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            movies.append(row)
    return movies


def get_serialized_movies():
    return [Movie(movie[0], movie[1], movie[2].split('|')).__dict__ for movie in get_movies_data()]


def get_ratings_data():
    ratings = []
    with open('src/data/ratings.csv', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            ratings.append(row)
    return ratings[1:]


def get_serialized_ratings():
    return [Rating(int(rating[0]), int(rating[1]), float(rating[2]), int(rating[3])).__dict__ for rating in
            get_ratings_data()]


def get_tags_data():
    tags = []
    with open('src/data/tags.csv', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            tags.append(row)
    return tags[1:]


def get_serialized_tags():
    return [Tag(int(tag[0]), int(tag[1]), str(tag[2]), int(tag[3])).__dict__ for tag in
            get_tags_data()]


def get_links_data():
    links = []
    with open('src/data/links.csv', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            links.append(row)
    return links[1:]


def get_serialized_links():
    return [Link(int(link[0]), int(link[1]), int(link[2] or 0)).__dict__ for link in
            get_links_data()]
