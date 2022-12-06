# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]



# ============================= мое решение с негафибоначи
a = b = 1
n = int(input('Задайте число: ')) 
print(a, b, end=' ') 

for i in range(2, n):
    a, b = b, a + b
    print(b, end=' ')

print('\n')
c = d = -1
print(c, d, end=' ') 
for i in range(2, n):
    c, d = d, c + d
    print(d, end=' ')



# ================== мой код фибоначи
# def Fibonachi(k):
#     if k in (1, 2):
#         return 1
#     else: 
#         return Fibonachi(k-1) + Fibonachi(k-2)
# k = int(input('Введите число : '))
# print(Fibonachi(k))




# ====================решение преподователя:
# def fibonacciPos(n):
#     a, b = 1, 1
#     for n in range(n):
#         yield a
#         a, b = b, a + b

# dataPos = list(fibonacciPos(k))
# print(f' Для введенного вами числа {k} список чисел Фибоначи : {dataPos}')

# def fibonacciNeg(n):
#     a, b = 1, -1
#     for n in range(n):
#         yield a
#         a, b = b, a - b





# ====================неправильный , пропускает 1 элемент:
# n = int(input('Введите число: '))
# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, -1
#     for i in range (n):
#         fibo_nums.insert(0, a)    # .insert - возвращает в указанно е место в списке, в нашем варианте перед 0
#         a, b = b, a - b
#     return fibo_nums
# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))







# =============================просто код фибоначи
# def fib(n):
#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)

# print(fib(8))




# работающий код фибоначи
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(8))
