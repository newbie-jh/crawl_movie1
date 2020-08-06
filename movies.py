import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(URL)

soup = BeautifulSoup( response.text , 'html.parser')
mlist = soup.select("div.lst_wrap dt.tit a")

final_movie_data = []

for m in mlist:
        movie_data = {
            'title' : m.text,
            'code' : m['href'][28:]
        }

        final_movie_data.append(movie_data)

#     with open("./movies.csv" , 'a' , encoding='utf-8') as csvfile:
#             fieldnames = ["title","code"]
#             csvwriter = csv.DictWriter(csvfile,fieldnames)
#             csvwriter.writerow(movie_data)

headers = {
        'authority': 'movie.naver.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'iframe',
        'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=189069',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'NNB=46UTUQCIQYCV6; NRTK=ag^#all_gr^#1_ma^#-2_si^#0_en^#0_sp^#0; nx_ssl=2; csrf_token=aca1c145-9559-4ab4-9a5c-148a126a2b3c',
}


for movie in final_movie_data:
        movie_code = movie['code']

        params = (
                ('code', movie_code),
                ('type', 'after^'),
                ('isActualPointWriteExecute', 'false'),
                ('isMileageSubscriptionAlready', 'false'),
                ('isMileageSubscriptionReject', 'false'),
        )

        response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)

        soup = BeautifulSoup(response.text,'html.parser')

        # print(soup.select_one('div.score_reple > p > span[id*="ment"]').get_text())

        review = []
        score = []

        # print("="*15 + movie["title"] + "="*15)
        em = soup.select('div.star_score em')
        span = soup.select('div.score_reple > p span[id*="unfold"] > a')
        
        for e,s in zip(em, span):
                # print(s.text.strip())
                # print(e.text)
                if s == []:
                        s = soup.select_one('div.score_reple > p > span[id*="ment"]')

                review.append(s['data-src'])
                score.append(e.text)

        for s,r in zip(score,review):

                review_data = {
                        'score' : s,
                        'review' : r
                }

                with open("./review_data.csv" , 'a' , encoding='utf_8') as csvfile:
                        fieldnames = ["score","review"]
                        csvwriter = csv.DictWriter(csvfile,fieldnames)
                        csvwriter.writerow(review_data)

        
        




