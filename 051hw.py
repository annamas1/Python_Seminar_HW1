# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст: ')
d = 'абв'
list = [i for i in text.split() if d not in i]
print(f'Результат: {" ".join(list)}')


