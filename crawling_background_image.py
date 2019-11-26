import requests
from pprint import pprint
from decouple import config  # .env에 ID, SECRET 저장
from datetime import datetime, timedelta
import json
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


with open('movies.json', 'r', encoding='utf-8') as f:
    movie_datas = json.load(f)
Code = ''
BASE_BACK_URL_1 = f'https://movie.naver.com/movie/bi/mi/photoView.nhn?code={Code}&imageNid='
BASE_IMAGE_URL = 'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode='
BASE_URL_NAVER = 'https://openapi.naver.com/v1/search/movie.json'
ID = config('CLIENT_ID')
SECRET = config('CLIENT_SECRET')

HEADERS = {
    'X-Naver-Client-Id' : ID ,
    'X-Naver-Client-Secret' : SECRET, 
}

with open('movies.json', 'r', encoding='utf-8') as f:
    movie_datas = json.load(f)

with open('movie_2.json', 'r', encoding='utf-8') as f:
    movies = json.load(f) 

for movie_data in movie_datas:
    title = movie_datas[movie_data]['title']
    API_URL_NAVER = f'{BASE_URL_NAVER}?query={title}'
    response = requests.get(API_URL_NAVER, headers = HEADERS)
    data = response.json()
    # 영화코드 추출하는 구간
    try:
        i = data['items'][0]['link'].index('=')
        mvCode = data['items'][0]['link'][i+1:]
        url = f'https://movie.naver.com/movie/bi/mi/photoView.nhn?code={mvCode}&imageNid='
    except:
        pass
    # 배경화면 url 구현
    
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        # 원하는 이미지 코드 추출
        try:
            ss = soup.find("img", alt='STILLCUT')
            imageUrl = ss.get("src")
        except:
            pass
        # start = imageNid.find('https:')
        # end = imageNid.find('.jpg') + 4
        try:
            qq = imageUrl.find('?')
            url_result = imageUrl[0:qq]
        except:
            url_result = ''
 
        # for i in range(start, end):
        #     url_result += imageNid[i]
    # 이미지 코드를 기존 데이터에 추가
    for movie in movies:
        if movie['fields']['movieCd'] == movie_data:
            movie['fields']['backgroundImage'] = url_result

with open('movie.json', 'w',  encoding = 'utf-8') as make_file:
    json.dump(movies, make_file, ensure_ascii=False, indent="\t")