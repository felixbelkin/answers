def shortener(st):
    result = ''
    stack = []

    for char in st:
        if char == '(':
            stack.append(char)
        elif char == ')' and stack:
            stack.pop()
        elif not stack:
            result += char

    return result

text = "Hello (World (with (Python)))!"
output = shortener(text)
print(output) 
