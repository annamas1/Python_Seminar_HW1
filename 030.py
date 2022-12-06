# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# f = open("Semenar30.txt","w+")
# stroka = f.read().split()
# print(stroka)

print()
print('1.Задача: Удалить из текста все слова, содержащие ""абв""')
with open('Semenar30.txt', 'r', encoding = 'utf_8') as data:
    stroka = data.read().split()
print(f'В файле записано: {stroka}')
print('Удалили все слова с абв и получили: ')
print(' '.join([word for word in stroka if 'абв' not in word]))
print()