
# This program generates and prints an n×n matrix where each diagonal relative to the main diagonal is filled with increasing integers, starting with 0 on the main diagonal.

n=int(input())
a=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = abs(i - j)
for row in a:
    print(" ".join(map(str, row)))
