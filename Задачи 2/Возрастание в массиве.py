def is_increasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True

numbers = [1, 2, 3, 5, 7, 9]
result = is_increasing(numbers)
print(result) 

numbers = [1, 3, 5, 3, 7, 9]
result = is_increasing(numbers)
print(result)  