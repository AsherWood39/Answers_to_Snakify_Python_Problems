
# This program finds and prints the length of the longest contiguous segment of equal numbers in a sequence ending with 0.

c=mc=0
p1=None
while True:
    n=int(input())
    if n==0:
        break
    elif n == p1:
        c += 1
    else:
        mc = max(mc,c)
        c = 1
    p1=n
print(max(mc,c))
