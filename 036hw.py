# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

b = int(input('Введите количество элементов последовательности: '))
posl1 = [round(random.uniform(1, 30), ) for posl1 in range(b)]  
posl2 = []
print(f'Последовательность сформирована: {posl1}\n')

for i in posl1:
       if i in posl1:
        posl2 = [round(random.uniform(1, 30), ) for posl2 in range(b)]
print(f'Cписок неповторяющихся элементов исходной последовательности: {posl2}')


# import random

# b = int(input('Введите количество элементов последовательности: '))
# posl1 = [round(random.uniform(1, 30), ) for posl1 in range(b)]  # задала последовательность
# posl2 = []
# print(f'Последовательность сформирована: {posl1}\n')

# # for i in posl1:
# #        if i in posl1:
# #         posl2 = [round(random.uniform(1, 30), ) for posl2 in range(b)]
# for i in range(len(posl1)):
#         for j in range(len(posl1)):
#                 if posl1[i] == posl1[j] and i != j:
#                         break
#                 else:
#                        print(posl1[i])
# print(f'Cписок неповторяющихся элементов исходной последовательности: {posl2}')


# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i] == a[j] and i != j:
#             break
#         else:
#             print(a[i])





# a = [int(i) for i in input().split()]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i] == a[j] and i != j:
#             break
#         else:
#             print(a[i])




# numbers = list(map(int, input("Введите числа через пробел:\n").split()))
# print(numbers)
# new_numbers = []

# for i in numbers:
#     if i not in new_numbers:
#         new_numbers.append(i)
# print(new_numbers)



# def elements(nums):
#     nums = [int(i) for i in nums.split()]
#     return list(set(nums))

# nums = '1 2 2 3 455 66 66 2 1'
# print(elements(nums))




# a = [int(i) for i in input().split()]
# for i in range(len(a)):
#    flag = 1
#    for j in range(len(a)):
#       if a[i] == a[j] and i != j:
#          flag = 0
#          break
#    if flag:
#       print(a[i])