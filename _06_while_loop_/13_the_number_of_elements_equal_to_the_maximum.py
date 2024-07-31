
# This program counts and prints the number of occurrences of the largest element in a sequence of integers ending with the number 0.

largest=c=i=0
while True:
    n=int(input())
    if n==0:
        break
    if n > largest:
        largest = n
        c = 1
    elif n == largest :
        c += 1
    i+=1
print(c)
