def count_lucky_numbers(length):
    def count_ways(digits, left_sum, right_sum, pos):
        if pos == length:
            return left_sum == right_sum

        count = 0
        for digit in range(10):
            if pos < length // 2:
                count += count_ways(digits + str(digit), left_sum + digit, right_sum, pos + 1)
            elif pos == length // 2 and length % 2 == 1:
                count += count_ways(digits + str(digit), left_sum, right_sum + digit, pos + 1)
            elif pos >= length // 2:
                count += count_ways(digits + str(digit), left_sum, right_sum + digit, pos + 1)

        return count

    count = 0
    for start_digit in range(1, 10):
        count += count_ways(str(start_digit), start_digit, 0, 1) * 2  # умножаем на 2 из-за симметрии

    return count

# Пример использования:
length = 4
result = count_lucky_numbers(length)
print(f"Количество счастливых чисел длины {length}: {result}")
