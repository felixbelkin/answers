def reverse_string_with_case_change(input_string):
    reversed_string = input_string[::-1]  # Переворачиваем строку с помощью среза

    # Изменяем регистр каждой буквы в перевернутой строке
    reversed_string = ''.join(
        char.upper() if char.islower() else char.lower() for char in reversed_string
    )

    return reversed_string

input_text = "Hello, World!"
result = reverse_string_with_case_change(input_text)
print(result)  

