
# This program finds and prints the greatest integer x such that 2^x is less than or equal to a given integer N, along with the value of 2^x, without using the ** operator.

n=int(input())
ex=0
i=1
while i*2<=n:
    i*=2
    ex+=1
print(ex,i)
    
