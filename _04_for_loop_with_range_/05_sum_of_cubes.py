
# This program calculates the sum of the series 13 + 23 + ... + N^3 for a given integer N.

n=int(input())
s=0
for i in range(1,n+1):
    s+=i**3
print(s)
