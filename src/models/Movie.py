import csv
from dataclasses import dataclass


class Movie:
    def __init__(self, id, name, genres) -> None:
        self.id = id
        self.name = name
        self.genres = genres

