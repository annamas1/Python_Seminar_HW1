# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N



number = int(input("Задайте число: "))
print('Список простых множителей: ')
for i in range(1, number+1):
    if(number%i==0):
        print(i)




# N = int(input('Введите число: '))
# d = 2
# while d*d <= N:
#     if N/d == 0:



# n=int(input("Integer: ")) 
# factors = []
# d = 2
# while d * d <= n:
#         if n % d == 0:
#             factors.append(d)
#             n//=d
#         else:
#             d += 1
#         if n > 1:
#             factors.append(n)
#         else:
#             break
# print('{} = {}' .format(n,factors))




# n = int(input("Введите число N: "))
# i = 2
# list = []

# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n //= i
#         i = 2
# else:
#     i += 1
# print(f"Простые множители введенного числа указаны в списке: {list}")




# n = int(input())
# r = 2
# g = n
# numbers = []
# for i in range(1, n):
#     if(g % r == 0):
#         numbers.append(r)
#         g = g // r
#     else:
#         r += 1

# print(numbers)




# def Factor(n):
#     Ans = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             Ans.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         Ans.append(n)
#     return Ans