import itertools


class Product:
    id = itertools.count()

    def __init__(self, name) -> None:
        self._id = next(Product.id)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f'Product ID: {self._id}, name: {self._name}'
