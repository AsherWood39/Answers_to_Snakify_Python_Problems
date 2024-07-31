
# This program calculates and prints the length of a sequence of non-negative integers, stopping when encountering a zero, without counting the zero itself or any numbers that follow it.

c=i=0
while True:
    if int(input())==0:
        break
    else:
        c+=1
    i+=1
print(c)
