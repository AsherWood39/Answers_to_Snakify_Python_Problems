
# This program reads a positive real number and prints the first digit to the right of the decimal point.

n=float(input())
n*=10
print(int(n%10))
