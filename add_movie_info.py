import requests
from pprint import pprint
from decouple import config  # .env에 ID, SECRET 저장
from datetime import datetime, timedelta
import json
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

BASE_URL_MINFO = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
BASE_URL_NAVER = 'https://openapi.naver.com/v1/search/movie.json'
KEY = config('KEY')
ID = config('CLIENT_ID')
SECRET = config('CLIENT_SECRET')


HEADERS = {
    'X-Naver-Client-Id' : ID ,
    'X-Naver-Client-Secret' : SECRET, 
}

with open('movies.json', 'r', encoding='utf-8') as f:
    movie_datas = json.load(f)

for movie_data in movie_datas:
    title = movie_datas[movie_data]['title']
    API_URL_NAVER = f'{BASE_URL_NAVER}?query={title}'
    response = requests.get(API_URL_NAVER, headers = HEADERS)
    data = response.json()

    if len(data['items']) >= 1:
        # 줄거리
        paragraph_data_header = ""
        paragraph_data_body = ""

        with urllib.request.urlopen(data['items'][0]['link']) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            try:
                paragraph_data_header = soup.find('h5', class_='h_tx_story').get_text()
            except:
                pass
            try:
                paragraph_data_body = soup.find('p', class_='con_tx').get_text()
            except:
                pass
            movie_datas[movie_data]['description'] = [paragraph_data_header, paragraph_data_body]


        # 이미지 url
        movie_datas[movie_data]['image'] = data['items'][0]['image']


        # 감독정보
        directors = list(map(str, data['items'][0]['director'].split('|')))
        directors.pop()
        movie_datas[movie_data]['directors'] = directors

        
        #배우정보
        actors = list(map(str, data['items'][0]['actor'].split('|')))
        actors.pop()
        movie_datas[movie_data]['actors'] = []
        if len(actors) > 3:
            for i in range(3):
                movie_datas[movie_data]['actors'].append(actors[i])
        else:
            movie_datas[movie_data]['actors'] = actors

        # 개봉년도 정보
        movie_datas[movie_data]['pubdate'] = data['items'][0]['pubDate']

        # 점수
        movie_datas[movie_data]['score'] = data['items'][0]['userRating']

        # 장르
        movie_datas[movie_data]['genres'] = []
        api_url = f'{BASE_URL_MINFO}?key={KEY}&movieCd={movie_data}'

        response = requests.get(api_url)
        data = response.json()
        for a in data['movieInfoResult']['movieInfo']['genres']:
            movie_datas[movie_data]['genres'].append(a['genreNm'])
    else:
        print(movie_data)
      
with open('movies_final.json', 'w',  encoding = 'utf-8') as make_file:
    json.dump(movie_datas, make_file, ensure_ascii=False, indent="\t")