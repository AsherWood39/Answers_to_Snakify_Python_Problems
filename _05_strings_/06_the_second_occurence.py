
# This program prints the index of the second occurrence of the letter 'f' in a given string, -1 if 'f' appears only once, or -2 if 'f' does not appear.

s=input()
if s.count('f')==1:
    print(-1)
elif s.count('f')==0:
    print(-2)
else:
    print(s.find('f',s.find('f')+1))
