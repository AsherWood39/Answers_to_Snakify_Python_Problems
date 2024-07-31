
# This program reads a three-digit number and prints the sum of its digits.

n=int(input())
s=0
for i in range(0,3):
    s+=n%10
    n//=10
    i+=1
print(s)
