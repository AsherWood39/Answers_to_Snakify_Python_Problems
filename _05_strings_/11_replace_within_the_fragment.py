
# This program replaces every occurrence of the letter 'h' with 'H' in a given string, except for the first and last occurrences.

s=input()
print(s[:s.find('h')+1]+s[s.find('h')+1:s.rfind('h')].replace('h','H')+s[s.rfind('h'):])
