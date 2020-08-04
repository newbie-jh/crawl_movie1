import requests
from bs4 import BeautifulSoup
import csv 


URL = 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(URL)

soup = BeautifulSoup( response.text , 'html.parser')
mlist = soup.select("div.lst_wrap dt.tit a")

for m in mlist:
    new_data = {
            'title' : m.text,
            'code' : m['href'][28:]
    }

    with open("./movies.csv" , 'a' , encoding='utf-8') as csvfile:
            fieldnames = ["title","code"]
            csvwriter = csv.DictWriter(csvfile,fieldnames)
            csvwriter.writerow(new_data)
