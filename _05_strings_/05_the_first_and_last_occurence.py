
# This program prints the index of the first and last occurrence of the letter 'f' in a given string, or just the index if 'f' occurs only once, without using loops.

s=input()
if s.count('f')==1:
    print(s.find('f'))
if s.count('f')>=2:
    print(s.find('f'),s.rfind('f'))
