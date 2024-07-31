
# This program determines if a chocolate bar of size n×m can be split into two rectangular parts such that one part has exactly k squares, and prints YES or NO.

n=int(input())
m=int(input())
k=int(input())

if k<n*m and (k%n==0 or k%m==0):
    print("YES")
else:
    print("NO")
