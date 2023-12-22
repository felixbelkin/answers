from collections import Counter

def count_it(sequence):
    # Создаем словарь для подсчета количества каждой цифры в строке
    count_dict = dict(Counter(map(int, sequence)))

    # Сортируем словарь по убыванию значений и выбираем три наиболее часто встречающихся числа
    top_3 = dict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:3])

    return top_3

result = count_it('1234423516')
print(result) 