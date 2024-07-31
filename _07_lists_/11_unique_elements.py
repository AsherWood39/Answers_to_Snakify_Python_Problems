
# This program finds and prints the elements that appear only once in a list, maintaining their original order.

n=input()
l=[int(x) for x in n.split()]
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i]==l[j] and i!=j:
            c+=1
    if c==0:
        print(l[i],end=' ')
    
