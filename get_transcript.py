import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.ted.com/talks/mariana_atencio_what_makes_you_special/transcript")
text = req.text

soup = BeautifulSoup(text, 'html.parser')
print(soup.p)