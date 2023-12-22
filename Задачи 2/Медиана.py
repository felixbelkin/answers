def median(numbers):
    numbers.sort()  # Сортировка списка чисел по возрастанию

    n = len(numbers)
    if n % 2 == 0:
        # Если количество чисел четное, медиана - среднее арифметическое двух чисел посередине
        middle_right = n // 2
        middle_left = middle_right - 1
        median_value = (numbers[middle_left] + numbers[middle_right]) / 2
    else:
        # Если количество чисел нечетное, медиана - число в середине списка
        median_index = n // 2
        median_value = numbers[median_index]

    return median_value

# Пример использования:
numbers = [7, 2, 3, 1, 5, 4, 6]
result = median(numbers)
print(f"Медиана ряда чисел: {result}")
