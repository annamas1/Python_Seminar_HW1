# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

n=float(input('Введите число '))
num=n*10
if (num%10==0):
    print('нет дробной части')
else: print(int(n*10%10))