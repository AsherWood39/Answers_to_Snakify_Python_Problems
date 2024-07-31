
# This program calculates and prints the nth Fibonacci number using a recursive function, demonstrating the slower performance of recursion compared to loops.

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(int(input())))
