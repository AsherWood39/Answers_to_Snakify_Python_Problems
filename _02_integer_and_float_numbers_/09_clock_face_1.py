
# This program calculates and prints the angle of the hour hand on a 12-hour clock based on hours, minutes, and seconds since midnight.

h=int(input())
m=int(input())
s=int(input())
a=(h*30+m*30/60+s*30/3600)
print(a)
