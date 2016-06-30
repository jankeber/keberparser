import praw
from bs4 import BeautifulSoup
import urllib
import sqlite3
import datetime
import os

if not os.path.exists('database'):
    conn = sqlite3.connect('database')
    conn.execute("CREATE TABLE weather (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, time TEXT NOT NULL, air_temp TEXT NOT NULL, wind_data TEXT NOT NULL, humidity_data TEXT NOT NULL, air_pressure TEXT NOT NULL, solar_power TEXT NOT NULL)")

conn = sqlite3.connect('database')
conn.text_factory = str
page = urllib.urlopen('http://193.95.233.105/econova1/Default.aspx?mesto=Koper');
pagesoup = BeautifulSoup(page)

page_title = str(pagesoup.find(id="MainContent_Label14").get_text().encode('utf-8'))
air_temp = str(pagesoup.find(id="MainContent_Label1").get_text().encode('utf-8'))
wind_data = str(pagesoup.find(id="MainContent_Label5").get_text().encode('utf-8'))
humidity_data = str(pagesoup.find(id="MainContent_Label2").get_text().encode('utf-8'))
air_pressure = str(pagesoup.find(id="MainContent_Label4nova").get_text().encode('utf-8'))
solar_power = str(pagesoup.find(id="MainContent_Label3").get_text().encode('utf-8'))

timedate = datetime.datetime.now()
time = timedate.hour

conn.execute("INSERT INTO weather (time, air_temp, wind_data, humidity_data, air_pressure, solar_power) VALUES (?, ?, ?, ?, ?, ?)", (time, air_temp, wind_data, humidity_data, air_pressure, solar_power))
conn.commit()

print page_title
print air_temp
print wind_data
print humidity_data
print air_pressure
print solar_power

print '======== REDDIT FEED ======='
print ''
print '======== REDDIT TECHNOLOGY ====='
red = praw.Reddit(user_agent='tomrel - private reader')
posts = red.get_subreddit('technology').get_hot(limit=20)
for x in posts:
    print x
print ''

print ''
print '======== REDDIT FORMULA 1 ========'
posts = red.get_subreddit('formula1').get_hot(limit=20)
for x in posts:
    print x

print ''
print '======= REDDIT PRIVACY ========='
posts = red.get_subreddit('privacy').get_hot(limit=20)
for x in posts:
    print x
print ''

print '====== PRIMORSKE NOVICE FEED ======='
primorske_url = "Http://primorske.si/"
primorske_feed = urllib.urlopen(primorske_url, 'html.parser')
primorske_soup = BeautifulSoup(primorske_feed)
primorske_find_all_h4 = primorske_soup.find_all("h4")
for primorske_a in primorske_find_all_h4:
    print primorske_a.get_text()