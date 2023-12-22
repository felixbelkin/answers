def multiply_numbers_from_string(numbers):
    numbers_list = list(map(int, numbers.split(', ')))
    from functools import reduce
    result = reduce(lambda x, y: x * y, numbers_list)

    return result

input_numbers = "2, 3, 4"
result = multiply_numbers_from_string(input_numbers)
print(f"Результат умножения чисел: {result}")
