# import requests
# from bs4 import BeautifulSoup
#
# page= requests.get("https://www.alx.pl/")
# soup = BeautifulSoup(page.content,'html.parser')
#
# soup = soup.find("ul", {"class", "main-nav"})
# soup = soup.find_all("li")
# soup = soup[0].find_all("a")
# for i in soup:
#     print(i.get_text())

# import requests
# from bs4 import BeautifulSoup
#
# page = requests.get("https://www.alx.pl/pl/kontakt/")
# soup = BeautifulSoup(page.content,'html.parser')
# soup = soup.find_all("p", {"class", "tel"})
# for i in soup:
#     print(i.get_text())

import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.alx.pl/pl/kontakt/")
soup = BeautifulSoup(page.content,'html.parser')
soup = soup.find_all("ul", {"class", "addresses"})
soup = soup[0].find("li")
print(soup)


