
# This program determines and prints the largest element in a sequence of integer numbers that ends with a zero, excluding the zero itself.

largest=i=0
while True:
    n=int(input())
    if n==0:
        break
    elif (n>largest):
        largest=n
    i+=1
print(largest)
