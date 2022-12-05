# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random
b = int(input('Задайте размер списка вещественных чисел = '))
list = [round(random.uniform(1.99, 10), 2) for list in range(b)]
max_list = max(list)
min_list = min(list)
N = max_list - min_list
print(f'{list} Pазница между максимальным и минимальным значением: {round(N, 2)}')


# рабочее решение:
# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))


# Решение преподователя (в мах 1 а в мин 0 потому что..)
# list = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in list:
#     if (i % 1) <= min:
#         min = i % 1
#     if ( i % 1) >= max:
#         max = i % 1
# print (f' Разница между максимальным и минимальным значением дробной части элементов {(max-min)}')