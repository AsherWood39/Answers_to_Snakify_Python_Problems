
# This program prints all elements from a list that are even numbers, using a for-loop to iterate directly over the list elements.

n=input()
l=[int(x) for x in n.split()]
for i in l:
    if i%2==0:
        print(i,end=' ')
