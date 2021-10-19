from typing import List, Union


def print_names(names: List[str]):
    for name in names:
        print(name)


def multiply_by_2_v1(numbers: List[Union[int, float]]):
    return [number * 2 for number in numbers]


def multiply_by_2_v2(numbers: List[Union[int, float]]):
    multiplied_array = []
    for number in numbers:
        multiplied_array.append(number * 2)
    return multiplied_array


def print_even(numbers: List[Union[int, float]]):
    try:
        for number in range(10):
            if numbers[number] % 2 == 0:
                print(numbers[number])
    except IndexError:
        print("List is too short")


def print_even_index(numbers: List[Union[int, float]]):
    try:
        for number in range(10):
            if number % 2 != 0:
                print(numbers[number])
    except IndexError:
        print("List is too short")


if __name__ == '__main__':
    print_names(["Lexus", "Jodie", "Martin", "Marilyn", "Bunny"])
    print(multiply_by_2_v1([1, 6, 2, 4, 8]))
    print_even([1, 8, 3, 5, 9, 2, 4, 8, 11, 5])
    print_even_index([1, 8, 3, 5, 9, 6, 2, 4, 8, 11])
