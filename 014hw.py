# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# ===============================================
# 1-й вариант решения, но не получилось с дробным числом, работает только для целого:

# cheslo = int(input("Введите число: "))
# sum = 0

# while cheslo > 0:
#     sum = sum + cheslo % 10
#     cheslo = cheslo // 10
# print(f'Сумма цифр = {sum}')

# ===============================================
# 2-й вариант решения работает только с дробным числом:

# cheslo = input("Введите дробное (через точку) : ")
# x = cheslo.split(".")
# a = int(x[0]) # целая часть
# b = int(x[1]) # дробная часть
# sum = 0
# while (a != 0): 
#     sum = sum + a % 10
#     a = a // 10
# while (b != 0):
#     sum = sum + b % 10
#     b = b // 10
# print("Произведение цифр равно:", sum)

#cheslo = input("Введите число (через точку) : ")

# ===============================================
# 3-й вариант решения универсальный работает со всеми:


n = input(("Введите число: "))
sum = 0
 
for i in n:
    if i.isdigit():
        sum += int(i)
        
print("Сумма:", sum)



# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))



# s = '0.56'
# summ = 0
# for i in s:
#     if i.isdigit():
#         summ += int(i)
# print(summ)
