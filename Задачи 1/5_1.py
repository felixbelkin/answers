def search_substr(subst, st):
    if subst.lower() in st.lower():
        return 'Есть контакт!'
    else:
        return 'Мимо!'

substring = 'abc'
string = 'xYzABcDeF'

result = search_substr(substring, string)
print(result)  