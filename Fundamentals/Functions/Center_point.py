import math


def coordinates(x1,y1,x2,y2):
    if ((x1*x1) + (y1*y1)) > ((x2*x2) + (y2*y2)):
        print(f"({x2}, {y2})")
    elif ((x1*x1) + (y1*y1)) == ((x2*x2) + (y2*y2)):
        print(f"({x2}, {y2})")
    else:
        print(f"({x1}, {y1})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
coordinates(math.floor((int(x1))), math.floor(int(y1)), math.floor(int(x2)), math.floor(int(y2)))