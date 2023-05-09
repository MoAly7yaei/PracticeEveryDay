from math import *
from numpy import append

def run():
    x1,y1,x2,y2=0,0,0,0
    dx,dy=0,0


    sx1 = [-10,-10,0,8,16]
    sy1 = [20,20,3,17,-16]
    sx2 = [-10,0,8,10,-10]
    sy2 = [-18,3,17,-16,-18]

    slop = 0
    lengh = 0

    def count(x1,y1,x2,y2):
        dx = x2 - x1
        dy = y2 - y1
        try:
            slop = dy / dx
            slop = round(slop,2)
        except ZeroDivisionError as e:
            slop = None
        lengh = sqrt((abs(dx))**2 + (abs(dy))**2)
        lengh = round(lengh,2)
        return lengh,"    ", slop

    i = 0
    y_values=[]
    print("Lengh        Slop")
    for i in range(0,5):
        x1 = sx1[i]
        x2 = sx2[i]
        y1 = sy1[i]
        y2 = sy2[i]
        y_values.append(y1)
        y_values.append(y2)

        print(count(x1,y1,x2,y2))
        i += 1
    print("Max of y: ",max(y_values))
    print("Min of y: ",min(y_values))