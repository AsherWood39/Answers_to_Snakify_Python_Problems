
# This program determines if a king can move from the first cell to the second in one move on a chessboard, given their coordinates.

r1=int(input())
c1=int(input())
r2=int(input())
c2=int(input())

if (abs(c2-c1)<=1 and abs(r2-r1)<=1):
    print("YES")
else:
    print("NO")
