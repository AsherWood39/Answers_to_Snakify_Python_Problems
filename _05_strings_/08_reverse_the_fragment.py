
# This program reverses the sequence of characters between the first and last occurrences of the letter 'h' in a given string.

s = input()
print(s[:s.find('h')+1]+s[s.rfind('h')-1:s.find('h'):-1]+s[s.rfind('h'):])
