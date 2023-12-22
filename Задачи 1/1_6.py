def all_eq(lst):
    max_length = max(len(s) for s in lst)  # Находим длину самой длинной строки в списке

    # Дополняем строки нижними подчеркиваниями до максимальной длины
    new_list = [s.ljust(max_length, '_') for s in lst]

    return new_list

strings = ['apple', 'banana', 'pear', 'grapefruit']
result = all_eq(strings)
print(result)  # рез: ['apple____', 'banana__', 'pear_____', 'grapefruit']