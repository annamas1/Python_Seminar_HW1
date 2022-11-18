# Напишите программу, которая по заданному номеру четверти, которая 
#   показывает диапазон возможных координат точек в этой четверти (x и y).

def chetv(x,y):
    if((x>0)and(y>0)):
        res="первая четврть"
        print(res)
    if((x<0)and(y>0)):
        res = "вторая четврть"
        print(res)
    if((x<0)and(y<=0)):
        res = "третья четврть"
        print(res)
    if((x>0)and(y<0)):
        res = "четвертая четврть"
        print(res)
    return res
 
if __name__ == '__main__':
    x=float(input())
    y= float(input())
    chetv(x,y)