# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)

lst = [2, 3, 4, 5, 6]
mult_lst(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)



# решение преподователя:

# import random
# b = int(input('Введите кол-во чисел в списке for 2# = '))
# list_b = list(random.randint(0, 10) for i in range(b))
# print (list_b)
# proiz_b = list(list_b[i]*list_b[-1*(1+i)] for i in range(b//2+1*(b%2)))
# print(proiz_b)



#мое 1 тупое решение
# N = (2, 3, 5, 6)
# proizvedenie1 = 0
# proizvedenie2 = 0
# proizvedenie1 = N[0]*N[3]
# proizvedenie2 = N[1]*N[2]
# print(f"Произведение пар чисел списка равно: {proizvedenie1, proizvedenie2}")



# сложение
# N = input().split()
# for i in range(len(N)):
#     N[i] = int(N[i])
#     count = N[0:2]
#     count1 = N[2:]
#     result = map(sum, (count, count1))
# print(list(result))


