
# This program checks if the given year is a leap year based on the Gregorian calendar rules and prints LEAP or COMMON accordingly.

year=int(input())

if year%100!=0 and year%4==0 or year%400==0:
    print("LEAP")
else:
    print("COMMON")
