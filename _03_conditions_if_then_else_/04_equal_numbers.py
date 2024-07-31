
# This program determines and prints how many of the three integers are equal: 3 if all are the same, 2 if two are equal, or 0 if all are different.

n1=int(input())
n2=int(input())
n3=int(input())

if n1==n2==n3:
    print(3)
elif (n1!=n2!=n3!=n1):
    print(0)
else:
    print(2)
