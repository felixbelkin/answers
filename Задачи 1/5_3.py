from collections import Counter

def top3(st):
    # Удаляем пробелы и считаем символы
    st_without_spaces = st.replace(' ', '')
    counter = Counter(st_without_spaces)

    # Выбираем три наиболее часто встречаемых символа
    most_common = counter.most_common(3)

    # Формируем строку с результатами
    result = ', '.join(f"{char} - {count}" for char, count in most_common)

    return result

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
output = top3(text)
print(output) 
