
# This program converts an English-Latin dictionary into a Latin-English dictionary, printing each Latin word followed by its English translations in lexicographical order.

N=int(input())
latin_english_dict = {}
for _ in range(N):
    eng, trans = input().split(' - ')
    latin = trans.split(', ')
    for x in latin:
        if x in latin_english_dict:
            latin_english_dict[x].append(eng)
        else:
            latin_english_dict[x] = [eng]
print(len(latin_english_dict))
for latin, trans in sorted(latin_english_dict.items()):
    eng = sorted(trans)
    print(latin + ' - ' + ', '.join(eng))

