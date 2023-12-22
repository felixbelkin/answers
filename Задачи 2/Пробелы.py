def remove_extra_spaces(input_string):
    return ' '.join(input_string.split())

text_with_extra_spaces = "   Эта   строка   имеет  много   лишних  пробелов   "
result = remove_extra_spaces(text_with_extra_spaces)
print(result)  
