
# This program calculates and prints the sum of all elements in a sequence of non-negative integers, ending when encountering a zero, and excluding the zero itself from the sum.

c=i=0
while True:
    n=int(input())
    if n==0:
        break
    else:
        c+=n
    i+=1
print(c)
