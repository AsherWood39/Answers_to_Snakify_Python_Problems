
# This program creates an n×m matrix and fills it with a checkerboard pattern of '.' and '*', starting with '.' in the top left corner.

n,m=[int(i) for i in input().split()]
a=[["."]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (i+j)%2!=0:
            a[i][j]="*"

for row in a:
    print(" ".join(row))
