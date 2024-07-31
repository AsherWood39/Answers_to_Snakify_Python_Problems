
# This program capitalizes the first letter of each word in a line of lowercase ASCII words and prints the result using a custom capitalize() function.

s=input()
def capitalize(s):
    s_w=s.split(' ')
    for i in range(len(s_w)):
        s_w[i]=s_w[i][0].upper()+s_w[i][1:]
    s=' '.join(s_w)
    print(s)
capitalize(s)
