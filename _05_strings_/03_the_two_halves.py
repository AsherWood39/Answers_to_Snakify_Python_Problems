
# This program splits a given string into two nearly equal parts, with the center character in the first part if the length is odd, and prints them in reverse order (second part first, then first part).

s=input()
l=len(s)
print(s[(l+1)//2:]+s[:(l+1)//2])
