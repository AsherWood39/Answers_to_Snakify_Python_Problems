
# This program calculates and prints the number of days required to reach or exceed a target distance y, starting from x miles and increasing the distance by 10% each day.

x=int(input())
y=int(input())
c=1
while (x<y):
    c+=1
    x+=(x*10/100)
print(c)
