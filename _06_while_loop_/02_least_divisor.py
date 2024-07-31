
# This program finds and prints the smallest integer divisor greater than 1 for a given integer that is not less than 2.

n=int(input())
for i in range(2,n+1):
    if n%i==0:
        print(i)
        break
