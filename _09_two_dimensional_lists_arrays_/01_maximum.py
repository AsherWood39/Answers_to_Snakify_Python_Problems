
# This program finds and prints the index (row and column) of the maximum element in a matrix, prioritizing the smallest row number and then the smallest column number in case of ties.

max_row,max_col=0,0
m,n=[int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]
for row in range(m):
    for col in range(n):
        if a[row][col]>a[max_row][max_col]:
            max_row=row
            max_col=col
print(max_row,max_col)
