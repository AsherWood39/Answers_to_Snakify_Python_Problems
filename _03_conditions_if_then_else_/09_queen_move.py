
# This program determines if a queen can move from the first cell to the second in one move on a chessboard, given their coordinates.

r1=int(input())
c1=int(input())
r2=int(input())
c2=int(input())

if ((r2==r1) or (c2==c1) or abs(r2-r1)==abs(c2-c1)):
    print("YES")
else:
    print("NO")
