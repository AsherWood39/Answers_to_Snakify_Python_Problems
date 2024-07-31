
# This program calculates and prints the average of all elements in a sequence of non-negative integers, terminating when encountering a zero, and excluding the zero itself from the average calculation.

c=i=0
while True:
    n=int(input())
    if n==0:
        break
    else:
        c+=n
    i+=1
print(c/i)
