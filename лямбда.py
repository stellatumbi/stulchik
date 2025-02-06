from functools import reduce

def square_numbers(numbers: list) -> list:
    squared_list = map(lambda x: x ** 2, numbers)
    return list(squared_list)

def filter_even_numbers(numbers: list) -> list:
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    return list(even_numbers)

def multiply_numbers(numbers: list) -> int:
    product = reduce(lambda x, y: x * y, numbers)
    return product

def sum_of_squares_of_even_numbers(numbers: list) -> int:
     even_numbers = filter(lambda x: x % 2 == 0, numbers)
     squared_numbers = map(lambda x: x ** 2, even_numbers)
     sum_of_squares = reduce(lambda x, y: x + y, squared_numbers)
     return sum_of_squares


def word_length_map(input_string: str) -> dict:
    word_lengths = {}
    for word in input_string.split():
        word_lengths[word] = len(word)
    return word_lengths
