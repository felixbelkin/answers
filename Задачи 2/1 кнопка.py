def one_button_device(message):
    # Создаем словарь, определяющий количество нажатий кнопки для каждой буквы
    letter_presses = {
        'A': 1,
        'E': 5,
        'G': 7,
        # Другие буквы и количество нажатий для них
    }

    # Преобразуем текст сообщения к верхнему регистру
    message = message.upper()

    # Проходим по каждой букве в сообщении и выводим последовательность нажатий для каждой буквы
    for char in message:
        if char in letter_presses:
            presses = letter_presses[char]
            print(f"Нажать кнопку {presses} раз для буквы {char}")

# Пример использования:
message_to_type = "Hello, World!"
one_button_device(message_to_type)
