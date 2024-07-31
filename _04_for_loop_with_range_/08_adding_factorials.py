
# This program calculates and prints the sum of factorials from 1! to n! for a given integer n using a single loop.

s=0
fact=1
for i in range(1,int(input())+1):
    fact*=i
    s+=fact
print(s)
