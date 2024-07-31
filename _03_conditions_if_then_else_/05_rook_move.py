
# This program determines if a rook can move from the first cell to the second in one move on a chessboard, given their coordinates.

r1=int(input())
c1=int(input())
r2=int(input())
c2=int(input())

if (c1==c2 or r1==r2):
    print("YES")
else:
    print("NO")
