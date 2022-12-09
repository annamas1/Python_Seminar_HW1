# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". 
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.



# print((lambda x: 'ra' in x)(input()))


# contains = lambda s, sample='ra': sample in s
# s = input()
# print(contains(s))


x=input()
y='plr'
f=(lambda x,y: y in x)
print(f)