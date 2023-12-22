def sum_numbers_in_string(s):
    current_number = 0
    total_sum = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            total_sum += current_number
            current_number = 0

    # Добавляем последнее число к общей сумме
    total_sum += current_number

    return total_sum

# Пример использования:
input_string = "abc123def45ghi6"
result = sum_numbers_in_string(input_string)
print(result)  # Ожидаемый результат: 177 (123 + 45 + 6 = 177)
