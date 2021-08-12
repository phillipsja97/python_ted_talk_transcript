import requests
from bs4 import BeautifulSoup
import mysql.connector
import os
from dotenv import load_dotenv
import time

def main(args1):

  load_dotenv()

  DB_PASSWORD = os.getenv('PASSWORD')

  HOST = "localhost"  
  PORT=3306
  USERNAME = "root"
  PASSWORD = DB_PASSWORD
  DATABASE = "ted_talks"

  print(args1)
  url = f"https://www.ted.com/talks?page={args1}"
  print(url)
  req = requests.get(url)
  text = req.text

  db = mysql.connector.connect(
      host=HOST,
      port=PORT,
      user=USERNAME,
      password=PASSWORD,
      database=DATABASE
  )

  soup = BeautifulSoup(text, 'html.parser')
  for a in soup.find_all(class_="talk-link"):
    cursor = db.cursor(buffered=True)
    link = a.findNext('a', attrs={"data-ga-context":"talks"}, href=True)
    linkToAdd = link['href']
    title_data = a.find(class_="f-w:700 h9 m5")
    title_name = title_data.find('a', attrs={"data-ga-context":"talks"})
    title = title_name.get_text()
    names = a.find(class_="h12 talk-link__speaker")
    image = a.find('img')
    imagesrc = image['src']
    titleName = title.strip().replace("'", "")

    add_talk = ("INSERT INTO talks "
                "(talk_title, talk_author, talk_href, talk_image) "
                "VALUES (%s, %s, %s, %s)")

    talk_data = (titleName, names.text, linkToAdd, imagesrc)
    query = (f"SELECT talk_title FROM talks WHERE talk_title = '{titleName}'")

    cursor.execute(query, multi=True)
    rowcount = cursor.rowcount
    if (rowcount == 0 ) :
      cursor.execute(add_talk, talk_data)
      db.commit()
    else :
      next
    cursor.close()
 
  db.close()
  time.sleep(5)
