#1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# a = int(input())
# range(*(1,5,2))

# N = int(input("Введите размер списка: "))
# spam = list(range(-N, N+1))
# print(spam)


# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# a = float(input("Введите дробное число: "))
# spam = float_number(*a)
# print(spam)

#round(float_number, number_of_decimals)


for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))


