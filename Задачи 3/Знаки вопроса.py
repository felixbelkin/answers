def replace_end_symbols(s):
    i = len(s) - 1

    while i >= 0 and (s[i] == '?' or s[i] == '!'):
        i -= 1

    if i < len(s) - 1:
        return s[:i+1] + s[i+1:].lstrip('?').lstrip('!') + s[i]

    return s

# Пример использования:
text = "Привет??!?"
result = replace_end_symbols(text)
print(result)  # Ожидаемый результат: "Привет?!"

text = "Это текст с множеством!!! вопросов??!!"
result = replace_end_symbols(text)
print(result)  # Ожидаемый результат: "Это текст с множеством вопросов!"