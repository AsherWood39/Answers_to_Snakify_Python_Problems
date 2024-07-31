
# This program creates and prints an n×n matrix where the minor diagonal has 1, positions above it have 0, and positions below it have 2, with spaces between each character.

n=int(input())
a=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            a[i][j]=1
        elif i+j>n-1:
            a[i][j]=2
for row in a:
    print(" ".join(map(str, row)))
