
# This program calculates and prints the total number of votes for each candidate across all states, sorted alphabetically by candidate names.

n = int(input())
records = {}
for i in range(n):
    entry = input().split()
    name = entry[0]
    if name in records:
        records[name] += int(entry[1])
    else:    
        records[name] = int(entry[1])
for key in sorted(records.keys()):
    print(key,records[key])
