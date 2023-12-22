def to_dict(lst):
    return {item: item for item in lst}

my_list = ['apple', 'banana', 'cherry']
result_dict = to_dict(my_list)
print(result_dict)
