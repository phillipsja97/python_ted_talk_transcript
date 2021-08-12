import os
from bs4 import BeautifulSoup
import requests
import get_talks



url = "https://www.ted.com/talks?page={sys.argv[1]}"
req = requests.get(url)
text = req.text

soup = BeautifulSoup(text, 'html.parser')
pagination = soup.find_all(class_="pagination__item pagination__link")
index = len(pagination) - 1
page = pagination[index]
text = page.get_text()
print(text)

for x in range(1, int(text)):
  print(x)
  get_talks.main(x)
else:
  print("Finally finished!")
