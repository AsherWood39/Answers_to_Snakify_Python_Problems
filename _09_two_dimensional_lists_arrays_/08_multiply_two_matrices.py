
# This program computes and prints the product of an m×n matrix A and an n×r matrix B, resulting in an m×r matrix.

m,n,r=[int(i) for i in input().split()]
a=[[int(i) for i in input().split()] for j in range(m)]
b=[[int(i) for i in input().split()] for j in range(n)]
c=[[0]*r for _ in range(m)]
for i in range(m):
    for j in range(r):
        for k in range(n):
            c[i][j]+=a[i][k]*b[k][j]
for row in c:
    print(' '.join(map(str,row)))
