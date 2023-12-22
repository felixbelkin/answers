def biggest_dict(**kwargs):
    my_dict = {'first_one': 'we can do it'}  # Создание словаря с одним элементом

    for key, value in kwargs.items():
        my_dict[key] = value  # Обновление словаря my_dict новыми ключами и значениями

    return my_dict

result = biggest_dict(second_one='hello', third_one='world')
print(result)
