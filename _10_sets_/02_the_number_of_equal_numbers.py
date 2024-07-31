
# This program counts and prints the number of unique numbers that occur in both of two given lists using a single line of code.

print(len(set(input().split()) & set(input().split())))
