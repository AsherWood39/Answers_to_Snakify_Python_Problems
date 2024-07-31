
# This program calculates the factorial of a given integer n without using the math module.

fact=1
for i in range(1,int(input())+1):
    fact*=i
print(fact)
