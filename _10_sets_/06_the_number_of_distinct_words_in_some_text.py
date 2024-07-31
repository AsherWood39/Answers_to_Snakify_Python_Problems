
# This program counts and prints the number of distinct words from n lines of text, where words are sequences of non-whitespace characters.

n=int(input())

distinct_words = set()
for i in range(n):
        words=input().split()
        distinct_words.update(words)

print(len(distinct_words))
