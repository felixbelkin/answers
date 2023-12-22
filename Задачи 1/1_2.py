def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    else:
        print("Список должен содержать минимум два элемента")

my_list = [1, 2, 3, 4, 5]
change(my_list)
print(my_list)  