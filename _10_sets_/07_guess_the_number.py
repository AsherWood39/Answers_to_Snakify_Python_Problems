
# This program determines and prints all possible secret numbers from 1 to n based on Beatrice's guesses and Augustus's responses, listing all remaining possibilities in ascending order when Beatrice asks for help.

n=int(input())
possible_values=set(range(1,n+1))
while True:
    guess=input()
    if guess == "HELP":
        break
    guess=set(int(i) for i in guess.split())
    response=input()
    if response=="YES":
        possible_values&=guess
    else:
        possible_values-=guess
print(*sorted(possible_values))
