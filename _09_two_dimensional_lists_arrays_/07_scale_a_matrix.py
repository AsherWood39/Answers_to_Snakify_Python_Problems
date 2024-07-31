
# This program multiplies every entry in an m×n matrix by a given integer c and prints the resulting matrix.

m,n=[int(i) for i in input().split()]
a=[[int(i) for i in input().split()] for j in range(m)]
c=int(input())
for i in range(m):
    for j in range(n):
        a[i][j]*=c
for row in a:
    print(' '.join(str(elem) for elem in row))
