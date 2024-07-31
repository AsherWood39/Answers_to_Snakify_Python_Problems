
# This program prints YES if the two given cells on a chessboard are the same color, NO if they are different colors.

r1=int(input())
c1=int(input())
r2=int(input())
c2=int(input())

if ((r1+c1+r2+c2)%2==0):
    print("YES")

else:
    print("NO")

