
# This program determines and prints the number of even elements in a sequence of integer numbers that ends with a zero, excluding the zero itself.

c=i=0
while True:
    n=int(input())
    if n==0:
        break
    elif n%2==0:
        c+=1
    i+=1
print(c)
