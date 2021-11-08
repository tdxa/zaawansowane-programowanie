def is_even(number: int) -> bool:
    return number % 2 == 0


if __name__ == '__main__':
    print("Liczba parzysta" if is_even(5) else "Liczba nieparzysta")
