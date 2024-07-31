
# This program prints a sequence of integers in reverse order using recursion, ending with a 0 as the terminator.

def reverse():
    n=int(input())
    if n!=0:
        reverse()
        print(n)
print(0)
reverse()

