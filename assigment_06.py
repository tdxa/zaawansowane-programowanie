def combine_lists(array1: list, array2: list) -> list:
    return [number ** 3 for number in list(set(array1 + array2))]


if __name__ == '__main__':
    print(combine_lists([1, 2, 3, 4], [1, 2, 8, 9, 9]))
