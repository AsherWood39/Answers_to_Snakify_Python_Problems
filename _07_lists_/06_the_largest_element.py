
# This program finds and prints the largest element in a list along with its index, printing the index of the first occurrence if the largest value is not unique.

n=input()
l=[int(x) for x in n.split()]
largest=l[0]
index=0
for i in range(1,len(l)):
    if (l[i]>largest):
        largest=l[i]
        index=i
print(largest,index)
