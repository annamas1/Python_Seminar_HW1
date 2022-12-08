# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
k = int(input("Введите натуральную степень k = "))
spisok_koef = list()
for i in range(1, k + 2):
    spisok_koef.append(randint(1, 101))
a = list()
for i in range(len(spisok_koef)):
    if k == 1:
        a.append(f'{spisok_koef[i]}*x')
    elif k == 0:
        a.append(f'{spisok_koef[i]}')
    else:
        a.append(f'{spisok_koef[i]}*x**{k}')
    flag = randint(0, 1)
    if flag == 1:
        a.append('+')
    elif flag == 0:
        a.append('-')
    k -= 1

with open('file037hw.txt', 'w') as data:
    data.write(''.join(a))
data.close()


# import random


# def write_file(st):
#     with open('file33.txt', 'w') as data:
#         data.write(st)


# def rnd():
#     return random.randint(0,101)


# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
    

# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))



# решение от создателя курса:
# from random import randint

# k = int(input('Insert equation power: '))
# koefs = list()
# for i in range(1, k + 2):
#     koefs.append(randint(1, 100))

# ans = list()
# for i in range(len(koefs)):
#     if k == 1:
#         ans.append(f'{koefs[i]}*x')
#     elif k == 0:
#         ans.append(f'{koefs[i]}')
#     else:
#         ans.append(f'{koefs[i]}*x**{k}')
#     flag = randint(0, 1)
#     if flag == 1:
#         ans.append('+')
#     elif flag == 0:
#         ans.append('-')
#     k -= 1

# ans.pop(-1)
# ans.append('=0')
# fout = open('output.txt', 'w')
# fout.write(''.join(ans))
# fout.close()




# еще решение без файла
# from random import randint
# max_val=100
# k = int(input('Введите натуральную степень k:'))
# # коэфф. при старшей степени не должен быть равен 0
# koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
# poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])
# # Поиск и замены:
# poly=poly.replace('x^1+', 'x+')
# poly=poly.replace('x^0', '')
# poly+=('','1')[poly[-1]=='+']
# poly=(poly, poly[:-2])[poly[-2:]=='^1']
# print(poly)



# еще решение без файла
# from random import randint
# from sympy import symbols
# from math import prod
 
# max_val=100
# k = int(input('Введите натуральную степень k:'))
# # коэфф. при старшей степени не должен быть равен 0
# koeff=[randint(-max_val ,max_val) for i in range(k)]+[randint(1,max_val)]
# x = symbols('x')
# print (sum(map(prod,zip(koeff,[x**i for i in range(k+1)]))), '= 0')
