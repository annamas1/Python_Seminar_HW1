# 2. на входе a = [4, 3, -10, 1, 7, 12], получить на выходе из этого списка  а=[4, -10, 12, 3, 1, 7]

a = [4, 3, -10, 1, 7, 12]
print(a.insert(1, -10))  # добавление в указанный элемент
print(a.insert(2, 12)) 
print(a.insert(3, 3)) 
print(a.insert(5, 7))
print(a)

# простое решение
a = [4, 3, -10, 1, 7, 12]
a.sort(key=lambda x: x%2)
print(a)


# print(list1.append(11))  # добавление в конец
# print(list1)





