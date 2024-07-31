
# This program reads the daily distance a car can cover and the total distance, then prints the number of days required to cover the route.

n=int(input())
m=int(input())
if (m%n==0):
    print(m//n)
else:
    print(m//n+1)
