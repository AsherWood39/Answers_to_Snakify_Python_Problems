
# This program counts and prints the number of occurrences of each word in a text before its first appearance in the same line.

words = input().split()
occurrences = {}
for w in words:
    if w in occurrences:
        c = occurrences[w]
    else:
        c = 0
    print(c, end=' ')
    occurrences[w] = c + 1
