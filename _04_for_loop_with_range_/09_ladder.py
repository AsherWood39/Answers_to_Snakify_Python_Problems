
# This program prints a ladder of n steps, where each k-th step consists of integers from 1 to k, for a given integer n ≤ 9.

for i in range(1,int(input())+1):
    for j in range(1, i + 1):
        print(j,sep='', end="")
    print()
