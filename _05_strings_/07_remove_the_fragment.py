
# This program removes the first and last occurrence of the letter 'h' from a given string and all characters between them.

s=input()
print(s.replace(s[s.find('h'):s.rfind('h')+1],''))
