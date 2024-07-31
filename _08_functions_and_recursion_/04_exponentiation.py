
# This program calculates and prints a^n using recursion, without using loops, the ** operator, or the built-in math.pow() function.

def power(a,n):
    if n==0:
        return 1
    else:
        return a*power(a,(n-1))

a=float(input())
n=int(input())
print(power(a,n))
