# ДЗ Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# (4 задачи из прошлых семинаров переделать с использованием этих функций)


#==========================================================================
# 1 Задача
d = int(input('Введите цифру, обозначающую день недели от 1 до 7 : '))
if d <= 5:
    print(f'{d} является рабочим днем')
if d ==6 or d == 7 :
    print(f'{d} выходной день')
if d > 8:
    print(f'Ошибка, введи число от 1 до 7!;)')

# улучшение: (что-то не задалось(((()))))
d = int(input('Введите цифру, обозначающую день недели от 1 до 7 : '))
# if d <= 5:
#     print('раб день')
# elif print('выходной день'):
list = [i for i in range(1, 8) if i <= 5]
print(list)
#====================================================================

# Задача 2. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.    
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81

N=int(input('Введите число '))
num=-3
for i in range(N):
    print(num**i)

# улучшение:
N=int(input('Введите число '))
list = [(i*-3) for i in range(1, N+1)]
print (list)



#====================================================================
# Задача 3 : Подсчитать сумму цифр в вещественном числе.

number = float(input("Введите вещественное число: "))

lst = list(str(number).split('.'))
summ = 0
for i in lst:
    for j in i:
        summ += int(j)
print(f"Сумма цифр вещественного числа равна = {summ}")

# улучшение

new_sum = sum(map(int, str(number).replace('.', '')))
print(f"Сумма цифр вещественного числа равна = {new_sum}")