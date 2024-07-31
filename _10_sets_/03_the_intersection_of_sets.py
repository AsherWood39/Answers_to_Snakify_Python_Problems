
# This program finds and prints all numbers that occur in both of two given lists, in ascending order, using a single line of code.

print(*sorted(set(input().split()) & set(input().split()), key=int))
