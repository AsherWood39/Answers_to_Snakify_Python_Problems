
# This program determines if any pair of queens on a given 8×8 chess board can attack each other and prints "YES" if they can, otherwise "NO".

n=8
x=[]
y=[]
for i in range(n):
    a,b=[int(s) for s in input().split()]
    x.append(a)
    y.append(b)

correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')
