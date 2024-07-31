
# This program calculates and prints three sets of numerical color values from Alice's and Bob's cube sets: 

# 1. Colors in both sets, 
# 2. Colors only in Alice's set, 
# 3. Colors only in Bob's set. 
# Each set is printed with its count followed by the sorted color values.

N,M=[int(i) for i in input().split()]
a,b=set(),set()
for i in range(N):
    a.add(int(input()))
for j in range(M):
    b.add(int(input()))
print(len(a&b),*sorted(a&b),sep="\n")
