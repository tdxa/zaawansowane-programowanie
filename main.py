from magazine.Product import Product
from magazine.Order import Order

product1 = Product("apple")
product2 = Product("orange")

order = Order("Tom Jeffrey", [product1,product2])
print(order)