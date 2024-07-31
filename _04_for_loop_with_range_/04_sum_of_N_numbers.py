
# This program reads N integers from the input and prints their sum, where N is specified on the first line.
 
n=int(input())
s=0
for i in range(0,n):
    s+=int(input())
print(s)
