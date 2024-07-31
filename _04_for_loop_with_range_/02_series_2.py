
# This program prints all integers from A to B inclusively in ascending order if A < B, otherwise in descending order.

a=int(input())
b=int(input())

if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)
