import itertools

from magazine import Product
from magazine.utils import employee


class Order:
    id = itertools.count(1)

    def __init__(self, client: str, products: list[Product]) -> None:
        self._id = next(Order.id)
        self._employee = employee
        self._client = client
        self._products = products

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        self._products = value

    def __str__(self) -> str:
        return f"Order ID: {self._id}\n" \
               f"Employee:{self._employee}\n" \
               f"Client:{self._client}\n" \
               f"Products:{self._products}"
