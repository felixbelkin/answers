def mul_to_int(a, b):
    result = a * b

    if isinstance(result, float) and result.is_integer():
        return int(result)
    else:
        return float(result)

print(mul_to_int(4, 5)) 
print(mul_to_int(2, 3.5)) 
print(mul_to_int(2.5, 4))  
print(mul_to_int(3.0, 2.0))  
