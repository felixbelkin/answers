def hacker_language(text):
    hacker_dict = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7'
    }

    # Проходим по строке и заменяем буквы на их эквиваленты
    encoded_text = ''
    for char in text:
        if char.lower() in hacker_dict:
            encoded_text += hacker_dict[char.lower()]
        else:
            encoded_text += char

    return encoded_text

# Пример использования:
original_text = "Hello, I am a hacker!"
encoded_text = hacker_language(original_text)
print(f"Исходный текст: {original_text}")
print(f"Закодированный текст на х4к3рском языке: {encoded_text}")
