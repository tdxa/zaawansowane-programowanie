def list_includes(array: list, number: int) -> bool:
    return number in array


if __name__ == '__main__':
    print(list_includes([1, 2, 3, 4], 63))
