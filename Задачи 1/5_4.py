def camel(st):
    result = []
    to_upper = True  # Первая буква будет в верхнем регистре

    for char in st:
        if char.isalpha():  # Проверяем, является ли символ буквой
            if to_upper:
                result.append(char.upper()) if char.islower() else result.append(char)
                to_upper = False
            else:
                result.append(char.lower()) if char.isupper() else result.append(char)
                to_upper = True
        else:
            result.append(char)  # Добавляем пробелы и знаки препинания без изменений

    return ''.join(result)

text = "Hello World! How are you?"
output = camel(text)
print(output) 
