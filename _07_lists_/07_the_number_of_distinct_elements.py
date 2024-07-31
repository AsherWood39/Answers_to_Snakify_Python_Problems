
# This program counts and prints the number of distinct elements in a sorted list.

n=input()
l=[int(x) for x in n.split()]
c=0
for i in range(len(l)):
    if (l[i] not in l[:i]):
        c+=1
print(c)
