
# This program prints "YES" if a number in the sequence has already been encountered and "NO" otherwise, for each number in the sequence.

def check_encountered_numbers():
    encountered = set()
    for num in input().split():
        if num in encountered:
            print("YES")
        else:
            print("NO")
            encountered.add(num)

check_encountered_numbers()
