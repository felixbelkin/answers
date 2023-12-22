# Создаем словарь с количеством элементов не менее 5
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}

# Поменяем местами первый и последний элементы словаря
keys = list(my_dict.keys())
values = list(my_dict.values())
keys[0], keys[-1] = keys[-1], keys[0]
values[0], values[-1] = values[-1], values[0]

# Удаляем второй элемент
del keys[1]
del values[1]

# Обновляем словарь с новыми ключами и значениями
my_dict.clear()
my_dict.update(zip(keys, values))

# Добавляем новый ключ 'new_key' со значением 'new_value' в конец словаря
my_dict['new_key'] = 'new_value'

# Выводим итоговый словарь
print(my_dict)
