import sys
import json
import requests
from bs4 import BeautifulSoup
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv('PASSWORD')

HOST = "localhost"
PORT=3306
USERNAME = "root"
PASSWORD = DB_PASSWORD
DATABASE = "ted_talks"

url = "https://www.ted.com/talks?page={sys.argv[1]}"
req = requests.get(url)
text = req.text

db = mysql.connector.connect(
    host=HOST,
    port=PORT,
    user=USERNAME,
    password=PASSWORD,
    database=DATABASE
)
cursor = db.cursor()

add_talk = ("INSERT INTO talks "
               "(talk_title, talk_author, talk_href, talk_image) "
               "VALUES (%s, %s, %s, %s)")


soup = BeautifulSoup(text, 'html.parser')
result = []
for a in soup.find_all(class_="talk-link"): 
  link = a.findNext('a', attrs={"data-ga-context":"talks"}, href=True)
  linkToAdd = link['href']
  title_data = a.find(class_="f-w:700 h9 m5")
  title_name = title_data.find('a', attrs={"data-ga-context":"talks"})
  title = title_name.get_text()
  names = a.find(class_="h12 talk-link__speaker")
  image = a.find('img')
  imagesrc = image['src']

  talk_data = (title.strip(), names.text, linkToAdd, imagesrc)
  cursor.execute(add_talk, talk_data)
  db.commit()

cursor.close()
db.close()
