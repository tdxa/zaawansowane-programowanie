from typing import Union


class Student:
    def __init__(self, name: str, mark: int):
        self.name = name
        self.mark = mark

    def is_passed(self):
        return self.mark > 50


class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library at {self.street}, {self.city} {self.zip_code} " \
               f"is opened: {self.open_hours}, " \
               f"contact: {self.phone}"


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str,
                 zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"{self.first_name} {self.last_name} born in {self.birth_date} has been working in the " \
               f"library since {self.hire_date}. " \
               f"Contact details: {self.street}, {self.zip_code} {self.city}, {self.phone}"


class Order:
    def __init__(self, employee: Employee, student: Student, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Order placed by {self.student.name} on {self.order_date}.\n" \
               f"Books borrowed: {list(map(lambda book: book.title, self.books))}.\nRealized by {self.employee} "


class Book:
    def __init__(self, library: Library, title: str, publication_date: str, author_name: str, author_surname: str,
                 number_of_pages: int):
        self.title = title
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book \"{self.title}\" wrote by {self.author_name} {self.author_surname} " \
               f"has been published {self.publication_date}. Number of pages: {self.number_of_pages}. " \
               f"It's in the library: {self.library}"


class Property:
    def __init__(self, area: int, rooms: int, price: Union[float, int], address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property with {self.rooms} rooms, area of {self.area}m\u00b2 at {self.address} costs {self.price}"


class House(Property):
    def __init__(self, area: int, rooms: int, price: Union[float, int], address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + f". Plot: {self.plot}m\u00b2 "


class Flat(Property):
    def __init__(self, area: int, rooms: int, price: Union[float, int], address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + f". Flat at floor {self.floor}"


if __name__ == '__main__':
    # Zadanie 1
    lazy_student = Student(name="Bob", mark=35)
    super_student = Student(name="Alicia", mark=86)
    print(f'Bob passed? {lazy_student.is_passed()}')
    print(f'Alicia passed? {super_student.is_passed()}')
    # Zadanie 2
    library1 = Library("Katowice", "Warszawska 45", "40-858", "7:00-22:00", "896541237")
    library2 = Library("Chorzów", "Mickiewicza 12", "41-500", "8:00-18:00", "745632158")

    book1 = Book(library1, "Doctor Sleep", "2013", "Stephen", "King", 600)
    book2 = Book(library1, "The Fault in Our Stars", "2012", "John", "Green", 412)
    book3 = Book(library2, "The Bear and the Nightingale", "2017", "Katherine", "Arden", 587)
    book4 = Book(library1, "The Girl on the Train", "2015", "Paula", " Hawkins", 369)
    book5 = Book(library2, "A Dance with Dragons", "2011", "George R. R.", "Martin", 450)

    employee1 = Employee("Louella", "Sheppard", "2011-11-17", "1974-08-04", "Falconaire", "Lombardy Street 56",
                         "10-200", "635124089")
    employee2 = Employee("Patsy", "Giles", "2010-09-09", "1989-01-03", "Driftwood", "Montrose Avenue 12", "12-631",
                         "203459715")
    employee3 = Employee("Travis", "Griffin", "2019-04-30", "2000-01-20", "Westmoreland", "Montrose Avenue 80",
                         "09-651", "96745032")

    student3 = Student(name="Alex", mark=77)

    order1 = Order(employee1, super_student, [book2, book4, book1], "2021-09-14 09:25")
    order2 = Order(employee3, lazy_student, [book3, book5], "2021-10-10 12:45")

    print(order1)
    print(order2)

    # Zadanie 3
    house = House(150, 8, 15000000, "Leśna 14, 15-880 Lubliniec", 2100)
    flat = Flat(64, 4, 250000, "Dąbrowskiego 14a, 40-500 Chorzów", 4)
    print(house)
    print(flat)
