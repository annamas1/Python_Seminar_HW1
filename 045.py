# НОД

a = int(input('Первое число '))
b = int(input('Второе число '))
import math
print(" НОД двух чисел ", math.gcd(a, b))



# =========
a=20
b=75
while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(a)




# =========
if a < b :
    a, b = b, a

while b!=0:
    a, b = b, a % b

print(a)