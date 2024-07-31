
# This program performs various string manipulations on the given string:

# 1. Print the third character.
# 2. Print the second-to-last character.
# 3. Print the first five characters.
# 4. Print all but the last two characters.
# 5. Print characters with even indices.
# 6. Print characters with odd indices.
# 7. Print the string in reverse order.
# 8. Print every second character in reverse order, starting from the last one.
# 9. Print the length of the string.

s=input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

