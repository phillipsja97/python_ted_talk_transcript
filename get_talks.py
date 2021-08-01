import sys
import requests
from bs4 import BeautifulSoup

url = "https://www.ted.com/talks?page={sys.argv[1]}"
req = requests.get(url)
text = req.text

soup = BeautifulSoup(text, 'html.parser')
links_with_text = []
authors = []
imagesource = []
# for a in soup.find_all('a', attrs={"data-ga-context":"talks"}, href=True): 
for a in soup.find_all(class_="talk-link"): 
  link = a.findNext('a', attrs={"data-ga-context":"talks"}, href=True)
  links_with_text.append(link['href'])

names = soup.find_all(class_="h12 talk-link__speaker")
for child in names:
  authors.append(child.string)

images = soup.findAll('img')
for image in images:
  imagesource.append(image['src'])

print(authors)
print(links_with_text)
print(imagesource)