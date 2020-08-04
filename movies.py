import requests
# html 파싱하는데 도움을 준다.
from bs4 import BeautifulSoup
import csv 


URL = 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(URL)

soup = BeautifulSoup( response.text , 'html.parser')
# new_section = soup.select('div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > .news.mynews.section._prs_nws > ul > li  ')
mlist = soup.select("div.lst_wrap dt.tit a")

title = []
code = []

for m in mlist:
    print(m.text)
    print(m['href'][28:])

    new_data = {
            'title' : m.text,
            'code' : m['href'][28:]
    }

    with open("./movies.csv" , 'a' , encoding='utf-8') as csvfile:
            fieldnames = ["title","code"]
            csvwriter = csv.DictWriter(csvfile,fieldnames)
            csvwriter.writerow(new_data)

# news = new_section.select('dl > dt > a')
#  for news in new_section:


#      new = news.select_one(' dl > dt > a')
# #     print(new['title'], new['href'])
