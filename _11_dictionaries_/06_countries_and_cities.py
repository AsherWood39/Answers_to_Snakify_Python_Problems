
# This program maps and prints the country for each given city based on a list of countries and their cities.

country_city = {}
for _ in range(int(input())):
    word = input().strip().split()
    country = word[0]
    country_city[country] = word[1:]
for _ in range(int(input())):
    city = input()
    for key in country_city.keys():
        if city in country_city[key] :
            print(key)
            break
