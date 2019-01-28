import csv
import datetime

from bs4 import BeautifulSoup
import requests


website = 'https://www.basketball-reference.com/players/j/jamesle01.html'
r = requests.get(website)
soup = BeautifulSoup((r.content), "lxml")

table = soup.find("table", {"id" : "per_game"})

tbody = table.find("tbody")

records = []
for row in table.tbody('tr'):

    records.append({
        "Season": row.find("th", {"data-stat" : "season"}).getText(),
        "Age": row.find("td", {"data-stat" : "age"}).getText(),
    })

filename = 'LebronsStats.csv'
with open(filename, 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["Season", "Age"], lineterminator = '\n')

    writer.writeheader()
    writer.writerows(records)