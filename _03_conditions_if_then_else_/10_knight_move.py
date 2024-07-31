
# This program determines if a knight can move from the first cell to the second in one move on a chessboard, given their coordinates.

r1=int(input())
c1=int(input())
r2=int(input())
c2=int(input())

if ((abs(r2-r1),abs(c2-c1))in [(1,2),(2,1)]):
    print("YES")
else:
    print("NO")
