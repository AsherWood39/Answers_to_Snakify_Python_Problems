
# This program finds and prints the most frequently occurring word from given lines of text, breaking ties by selecting the word that is alphabetically smallest.

n = int(input())
word_count = {}
for _ in range(n):
    words = input().split()
    for w in words:
        if w in word_count:
            word_count[w]+=1
        else:
            word_count[w]=1

max_value = max(word_count.values())
word = []
for key in word_count.keys():
    if word_count[key] == max_value:
        word.append(key)
print(sorted(word)[0])
