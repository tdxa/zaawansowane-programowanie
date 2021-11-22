import itertools
from magazine.utils import message_product


class Product:
    id = itertools.count(1)

    def __init__(self, name) -> None:
        self._id = next(Product.id)
        self._name = name
        message_product()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f'Product ID: {self._id}, name: {self._name}'
