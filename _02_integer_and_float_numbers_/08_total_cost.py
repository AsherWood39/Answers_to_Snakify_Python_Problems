
# This program calculates and prints the total cost in dollars and cents for purchasing N cupcakes priced at A dollars and B cents each.

a=int(input())
b=int(input())
n=int(input())
cost=n*(a*100+b)
print(cost//100,cost%100)
