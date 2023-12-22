def first_last(letter, st):
    first_index = st.find(letter)
    last_index = st.rfind(letter)

    if first_index == -1:  # Если символ не найден
        return (None, None)
    else:
        return (first_index, last_index)

result = first_last('a', 'example string with some letters')
print(result)  
