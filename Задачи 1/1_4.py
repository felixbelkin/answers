def useless(s):
    if len(s) > 0:
        max_number = max(s)  # Находим максимальное число в списке
        result = max_number / len(s)  # Делим максимальное число на длину списка
        return result
    else:
        return None  # Возвращаем None, если список пуст

numbers = [3, 8, 12, 6, 4]
useless_value = useless(numbers)
print(useless_value)  # Выведет результат деления максимального числа на длину списка
