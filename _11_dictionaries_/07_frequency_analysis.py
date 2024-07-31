
# This program prints all unique words from the input text in descending order of their frequency, and in lexicographical order for words with the same frequency.

text = [input().split() for _ in range(int(input()))]
word_count = {}
for line in text:
    for word in line:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
sorted_words = sorted(word_count.items(), key = lambda x: (-x[1], x[0]))

for word, freq in sorted_words:
    print(word)
