
# This program prints all squares of integer numbers less than or equal to a given integer N, in ascending order.

n=int(input())
i=1
while (i**2<=n):
    print(i**2,end=' ')
    i=i+1
