# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N=int(input('Введите число : '))
a=N
num=1

for i in range(N):
    num *= N
    N -= 1
print(f"Произведение чисел от 1 до {a} равно: ", (num))







# n = int(input())
# f = 1
# while n>1:
#     f *= n
#     n -= 1
# print (f)

# n=int(input())
# import math
# f = math.factorial(n)
# print(f)


