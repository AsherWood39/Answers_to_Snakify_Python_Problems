
# This program finds and prints a synonym for a given word based on a provided dictionary of word pairs where each pair consists of synonyms.

n=int(input())
dictionary={}
for i in range(n):
    words=input().strip().split()
    dictionary[words[0]]=words[1:]
search=input()
for key,val in dictionary.items():
    if search==key:
        print(*val)
        break
    elif search in val:
        print(key)
        break
        
