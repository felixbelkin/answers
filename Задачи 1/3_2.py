def help_bool(letter):
    if letter == 'к':
        return "Коммутативность: A and B = B and A, A or B = B or A"
    elif letter == 'а':
        return "Ассоциативность: A and (B and C) = (A and B) and C, A or (B or C) = (A or B) or C"
    elif letter == 'д':
        return "Дистрибутивность: A and (B or C) = (A and B) or (A and C), A or (B and C) = (A or B) and (A or C)"
    elif letter == 'м':
        return "Правило де Моргана: not (A and B) = not A or not B, not (A or B) = not A and not B"
    else:
        return "Пожалуйста, введите 'к', 'а', 'д' или 'м' для получения подсказки по соответствующему правилу."


print(help_bool('к'))  
print(help_bool('а'))  
print(help_bool('д'))  
print(help_bool('м'))  
print(help_bool('x'))  
