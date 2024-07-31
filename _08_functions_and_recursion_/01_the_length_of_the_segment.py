
# This program calculates and prints the Euclidean distance between two points given their Cartesian coordinates.

x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
def distance(x1,y1,x2,y2):
    import math
    print(math.sqrt((x2-x1)**2+(y2-y1)**2))
