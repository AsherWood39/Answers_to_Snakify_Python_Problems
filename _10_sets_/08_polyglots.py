
# This program determines and prints the languages spoken by all students and those spoken by at least one student, including their counts and lists in alphabetical order.

n=int(input())
languages=[]
for i in range(n):
    n_lang=int(input())
    st_lang=set()
    for _ in range(n_lang):
        st_lang.add(input())
    languages.append(st_lang)
    
common_lang=set.intersection(*languages)
n_common_lang=len(common_lang)

all_lang=set.union(*languages)
n_all_lang=len(all_lang)

print(n_common_lang,*sorted(common_lang),sep='\n')
print(n_all_lang,*sorted(all_lang),sep='\n')
