
# This program creates an n×n matrix with a snowflake pattern by filling the middle row, middle column, and diagonals with '*', and prints the matrix with characters separated by a single space.

n=int(input())
a=[["."]*n for _ in range(n)]
for i in range(n):
    a[i][n//2]=a[n//2][i]=a[i][i]=a[i][n-i-1]="*"
for row in a:
    print(' '.join(row))
