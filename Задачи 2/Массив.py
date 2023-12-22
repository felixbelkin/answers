def accumulate_numbers(arr):
    accumulated_array = []
    accumulated_sum = 0

    for num in arr:
        accumulated_sum += num
        accumulated_array.append(accumulated_sum)

    return accumulated_array

input_array = [1, 2, 3, 4, 5]
result = accumulate_numbers(input_array)
print(result)  