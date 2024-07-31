
# This program prints all elements from a list that have even indices (e.g., A[0], A[2], A[4], ...).

n=input()
l=[int(x) for x in n.split()]
for i in range(0,len(l),2):
    print(l[i],end=' ')
