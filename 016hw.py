# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.


N = int(input('Введите число:'))
num = [round((1+1/i)**i, 3) for i in range(1, N+1)]
print(f'Последовательность: {num}\n Сумма: {round(sum(num), 2)}')




# N = int(input('Введите число:'))
# num = (1+1/N)**N

# for i in range(N):
#     print(num**i)
# for d in range(N):
#     num += N
#     N -= 1
# print(f"Их сумма равна: ", (num))