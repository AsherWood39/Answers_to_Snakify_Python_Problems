
# This program counts and prints the number of zeros among N given integers, where N is specified as the first input.

c=0
for i in range(0,int(input())):
    n=int(input())
    if n==0:
        c+=1
print(c)
