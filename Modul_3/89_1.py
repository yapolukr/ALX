import requests

dane = requests.get('https://api.chucknorris.io/jokes/categories')
dane = dane.json()
print(dane)
for i in dane:
    print(i, end=" ")

print()

podajCategory = input('Podaj category: ')

dane = requests.get(f'https://api.chucknorris.io/jokes/random?category={podajCategory}')
dane = dane.json()
print(dane['value'].replace("Chuck Norris", "Yana Frolova"))




