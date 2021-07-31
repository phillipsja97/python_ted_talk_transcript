import sys
import requests
from bs4 import BeautifulSoup

url = "https://www.ted.com/talks?page={sys.argv[1]}"
req = requests.get(url)
text = req.text

page = BeautifulSoup(text, 'html.parser')
# all_links = [a['href'] for a in page.find_all('a', attrs={"data-ga-context":"talks"} , href=True)]
# needed_links = []
# for idx, item in enumerate(all_links):
#     print(item)
#     if idx % 2 == 0:
#       needed_links.append(item)


soup = BeautifulSoup(text, 'html.parser')
links_with_text = []
# for a in soup.find_all('a', attrs={"data-ga-context":"talks"}, href=True): 
for a in soup.find_all(class_="talk-link"): 
    if a.text:
      link = a.findNext('a', attrs={"data-ga-context":"talks"}, href=True)
      links_with_text.append(link['href'])

print(links_with_text)