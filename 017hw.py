# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число. НЕ ПОНЯЛА ЧТО ЭТО ЗНАЧИТ???
# Реализуйте алгоритм перемешивания списка.


N = int(input("Введите размер списка: "))
list = list(range(-N, N+1))
result = 1
print(list)    #список элементов, заполненных числами из промежутка [-N, N]
print([sum(list) - i for i in list])   # вроде как перемешала список, или не так надо было?!
for index in range(-N, N+1):
    result *= list[index]
print(f'Cписок элементов: {list}\nПроизведение: {result}')



# result = 1
# f = open('file.txt', 'r')
# for line in f:
#     if line == "":
#         break
#     result *= numbers[int(line)]
# f.close()
# print(result)



#правильное решение:

from random import randint
n = int(input('Введите число N - '))
numbers = []
for i in range(n):
    numbers.append(randint(-n, n+1))
print(numbers)

f = open('file.txt', 'w')
while True:
    s = input('Укажите позицию для вычисления - ')
    if s == "":
        break
    f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)

# Перемешивание списка 

# import random
# list = ["Anna", "Alex", 3.14159, 0]
# for i in range(len(list)):
#     index_a = random.randint(0, len(list) - 1)
#     temp = list[i]
#     list[i] = list[index_a]
#     list[index_a] = temp
# print(list)



# import random 
# y = ['Apple', '2 ', '-5675 ', '0.678 ', 'morning']
# random.shuffle(y)   # специальный метод для перемешивания списка
# print(y)

# a,b=b,a        # перемешивание