
# Converts two time inputs (hours, minutes, seconds) into total seconds and prints the difference.

h1=int(input())
m1=int(input())
s1=int(input())
h2=int(input())
m2=int(input())
s2=int(input())
s1+=m1*60+h1*3600
s2+=m2*60+h2*3600
print(s2-s1)
