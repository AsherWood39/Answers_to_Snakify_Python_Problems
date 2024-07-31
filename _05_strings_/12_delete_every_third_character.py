
# This program removes all characters from a given string whose indices are divisible by 3.

s=input()
print(''.join([s[i] for i in range(len(s)) if i % 3 != 0]))
