
# This program swaps the minimal and maximal elements in a list of unique numbers and prints the resulting list.

n=input()
l=[int(x) for x in n.split()]
min_i=0
max_i=0
for i in range(1,len(l)):
    if l[i]>l[max_i]:
        max_i=i
    if l[i]<l[min_i]:
        min_i=i
l[min_i],l[max_i]=l[max_i],l[min_i]
print(' '.join([str(i) for i in l]))
