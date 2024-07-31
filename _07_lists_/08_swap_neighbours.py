
# This program swaps adjacent items in pairs in a list (e.g., A[0] with A[1], A[2] with A[3], etc.) and prints the resulting list, leaving the last element in place if the list has an odd number of elements.

n=input()
l=[int(x) for x in n.split()]
for i in range(0,len(l)-1,2):
    l[i],l[i+1]=l[i+1],l[i]
print(' '.join([str(i) for i in l]))
