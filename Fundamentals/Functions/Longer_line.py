def coordinates(x1,y1,x2,y2):
    if ((x1*x1) + (y1*y1)) < ((x2*x2) + (y2*y2)):
        print(f"({x2}, {y2})")
    elif ((x1*x1) + (y1*y1)) == ((x2*x2) + (y2*y2)):
        print(f"({x2}, {y2})")
    else:
        print(f"({x1}, {y1})")


def coordinates2(x3,y3,x4,y4):
    if ((x3*x3) + (y3*y3)) < ((x4*x4) + (y4*y4)):
        print(f"({x4}, {y4})")
    elif ((x3*x3) + (y3*y3)) == ((x4*x4) + (y4*y4)):
        print(f"({x4}, {y4})")
    else:
        print(f"({x3}, {y3})")


def coordinates3(x1,y3,x2,y4):
    if ((x1*x1) + (y3*y3)) < ((x2*x2) + (y4*y4)):
        print(f"({x2}, {y4})")
    elif ((x1*x1) + (y3*y3)) == ((x1*x1) + (y4*y4)):
        print(f"({x2}, {y4})")
    else:
        print(f"({x1}, {y4})")


def coordinates4(x2,y4,x1,y3):
    if ((x2*x2) + (y4*y4)) < ((x1*x1) + (y3*y3)):
        print(f"({x1}, {y3})")
    elif ((x2*x2) + (y4*y4)) == ((x1*x1) + (y3*y3)):
        print(f"({x1}, {y3})")
    else:
        print(f"({x2}, {y4})")


def coordinates5(x1,y4,x2,y3):
    if ((x1*x1) + (y4*y4)) > ((x2*x2) + (y3*y3)):
        print(f"({x2}, {y3})")
    elif ((x1*x1) + (y4*y4)) == ((x1*x1) + (y3*y3)):
        print(f"({x2}, {y3})")
    else:
        print(f"({x1}, {y4})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
coordinates(x1,y1,x2,y2)
coordinates2(x3,y3,x4,y4)
coordinates3(x1,y3,x2,y4)
coordinates4(x2,y4,x1,y3)
coordinates5(x1,y4,x2,y3)