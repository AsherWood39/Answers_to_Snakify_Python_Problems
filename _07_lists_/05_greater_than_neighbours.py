
# This program counts and prints the number of elements in a list that are greater than both of their neighbors, excluding the first and last elements.

n=input()
c=0
l=[int(x) for x in n.split()]
for i in range(1,len(l)-1):
    if (l[i]>l[i-1] and l[i]>l[i+1]):
        c+=1
print(c)
