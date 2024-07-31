
# This program prints all elements in a list that are greater than the preceding element.

n=input()
l=[int(x) for x in n.split()]
for i in range(1,len(l)):
    if l[i]>l[i-1]:
        print(l[i],end=' ')
