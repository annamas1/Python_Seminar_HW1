# Рандом в функции:

# import random
# def x(b=None):   # нельзя написать тут т.к. одинаково будет, надо ниже писать
#     if b is None:
#         b = random.randint(1, 10)

#     a=b+1
#     print(a)
# x_random1=x()
# x_random2=x()


# =========== Задание 1:   НОД (несколько вариантов решений)


# a = int(input('Первое число '))
# b = int(input('Первое число '))
# import math
# print(' НОД двух чисел', math.gcd(a, b))



# a=int(input('Первое число '))
# b=int(input('Второе число '))
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a

# print(a)



a=int(input('Первое число '))
b=int(input('Второе число '))
if a < b :
    a, b = b, a

while b!=0:
    a, b = b, a % b
print(a)