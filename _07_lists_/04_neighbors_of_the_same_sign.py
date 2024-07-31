
# This program prints the first pair of adjacent elements in a list that have the same sign; if no such pair exists, the output is left blank.

n=input()
l=[int(x) for x in n.split()]
for i in range(len(l)-1):
    if (l[i] * l[i+1] > 0):
        print(l[i],l[i+1])
        break
