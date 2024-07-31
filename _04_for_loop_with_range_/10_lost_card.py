
# This program finds and prints the number on the lost card from a set of cards numbered 1 to N, given N-1 remaining distinct integers.

N = int(input())
list=[]
for i in range (1 , N):
    list.append(int(input())) 
for i in range(1 , N + 1):
    if i not in list:
        print(i)
