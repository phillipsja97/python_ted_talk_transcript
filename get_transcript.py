import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]
req = requests.get(url)
text = req.text

soup = BeautifulSoup(text, 'html.parser')
transcript = soup('p')
print(soup)