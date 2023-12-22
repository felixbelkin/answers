def has_double_letters(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False

input_word = "hello"
result = has_double_letters(input_word)
print(result)  
