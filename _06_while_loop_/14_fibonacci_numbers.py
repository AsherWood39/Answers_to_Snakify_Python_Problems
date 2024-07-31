
# This program calculates and prints the nth Fibonacci number using an iterative approach.

n=int(input())
p2 , p1 = 0 , 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(2, n + 1):
        f = p2 + p1
        p2, p1 = p1, f
    print(f)
