
# This program determines and prints the number of elements in a sequence of integer numbers (ending with zero) that are greater than their immediate neighbors. The zero at the end of the sequence is not considered.

c=i=0
p1=int(input())
while True:
    n=int(input())
    if n==0:
        break
    else:
        if n>p1:
            c+=1
        p1=n
    i+=1
print(c)
