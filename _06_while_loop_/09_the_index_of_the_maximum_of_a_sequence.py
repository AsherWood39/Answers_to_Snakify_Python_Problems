
# This program determines and prints the index of the first occurrence of the largest element in a sequence of integer numbers that ends with a zero, excluding the zero itself.

largest=index=0
i=1
while True:
    num=int(input())
    if num==0:
        break
    if num>largest:
        largest=num
        index=i
    i+=1
print(index)
