
# This program finds the index of a given number in the Fibonacci sequence or prints -1 if the number is not a Fibonacci number.

p2,p1=0,1
a=int(input())
i=0
while p1<a:
    p2,p1=p1,p1+p2
    i+=1
if p1==a:
    print(i+1)
else:
    print(-1)
