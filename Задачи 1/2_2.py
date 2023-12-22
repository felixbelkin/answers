def avg_5(a, b, c, d):
    average = (a + b + c + d) / 4  # Находим среднее арифметическое
    rounded_average = round(average, 5)  # Округляем до 5 знаков после запятой
    return rounded_average

result = avg_5(10, 20, 30, 40)
print(result)  
