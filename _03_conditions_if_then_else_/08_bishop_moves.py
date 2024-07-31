
# This program determines if a bishop can move from the first square to the second in one move on a chessboard, given their coordinates.

r1=int(input())
c1=int(input())
r2=int(input())
c2=int(input())

if (abs(r2-r1)==abs(c2-c1)):
    print("YES")
else:
    print("NO")
