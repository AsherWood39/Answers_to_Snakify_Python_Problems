
# This program counts and prints the number of unique pairs of elements in a list that have the same value, ensuring each pair is counted only once.

n=input()
l=[int(x) for x in n.split()]
c=0
for i in range(len(l)):
    for j in l[i+1:]:
        if l[i]==j:
            c+=1
print(c)
