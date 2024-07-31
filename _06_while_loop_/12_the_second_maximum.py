
# This program determines and prints the value of the second largest element in a sequence of distinct positive integers, which ends with the number 0. The sequence is guaranteed to have at least two elements.

largest=int(input())
second_largest=int(input())
if second_largest>largest:
    second_largest,largest=largest,second_largest
while True:
    n=int(input())
    if n==0:
        break
    elif (n>largest):
        second_largest,largest=largest,n
    elif(n>second_largest and n<largest):
        second_largest=n
print(second_largest)
