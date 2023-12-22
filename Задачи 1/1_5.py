import math

def list_sort(lst):
    return sorted(lst, key=lambda x: abs(x), reverse=True)

numbers = [-3, 5, -1, 8, -10]
sorted_numbers = list_sort(numbers)
print(sorted_numbers)
