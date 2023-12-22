def surrounded_by_plus(string):
    length = len(string)
    if length == 0:
        return True  # Пустая строка считается верным случаем

    for i in range(length):
        if string[i].isalpha():
            # Если текущий символ - буква, проверяем, окружен ли он знаками плюс
            if i == 0 or i == length - 1 or string[i - 1] != '+' or string[i + 1] != '+':
                return False

    return True

input_string = "++A++B++"
result = surrounded_by_plus(input_string)
print(result)  # Ожидаемый результат: True

input_string = "++C+D+E++"
result = surrounded_by_plus(input_string)
print(result)  # Ожидаемый результат: False
