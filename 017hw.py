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




