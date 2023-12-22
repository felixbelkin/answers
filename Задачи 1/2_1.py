def to_float(num):
    if isinstance(num, (int, float)):
        return float(num)
    else:
        return "Невозможно преобразовать"

print(to_float(5))  
print(to_float(10.75))
print(to_float("hello"))  
