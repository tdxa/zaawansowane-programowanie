# Assigment_01
def greetings(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}"


# Assigment_02
def multiply(num1: int, num2: int) -> int:
    return num1 * num2


# Assigment_03
def is_even(number: int) -> bool:
    return number % 2 == 0


# Assigment_04
def check_sum(num1: int, num2: int, num3: int) -> bool:
    return (num1 + num2) >= num3


# Assigment_05
def list_includes(array: list, number: int) -> bool:
    return number in array


# Assigment_06
def combine_lists(array1: list, array2:list) -> list:
    return [number**3 for number  in list(set(array1+array2))]


if __name__ == '__main__':
    print((greetings("Anna", "Domańska")))
    print(multiply(5, 10))
    result = is_even(5)
    print("Liczba parzysta" if result else "Liczba nieparzysta")
    print(check_sum(2, 10, 5))
    print(list_includes([1,2,3,4],63))
    print(combine_lists([1,2,3,4],[1,2,8,9,9]))
