#1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# 1 вариант решения:
# N = int(input())
# M = N*(-1)
# print(M)

# while N != M:
#     print(N)
#     N -= 1
# else:
#     print(N)
#     print('это все')


# 2 вариант решения:

N = int(input("Введите размер списка: "))
spam = list(range(-N, N+1))
print(spam)


# a = int(input())
# range(*(1,5,2))

