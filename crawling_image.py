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

with open('movie_1.json', 'r', encoding='utf-8') as f:
    movies = json.load(f) 

for movie_data in movie_datas:
    title = movie_datas[movie_data]['title']
    API_URL_NAVER = f'{BASE_URL_NAVER}?query={title}'
    response = requests.get(API_URL_NAVER, headers = HEADERS)
    data = response.json()
    try:
        i = data['items'][0]['link'].index('=')
        mvCode = data['items'][0]['link'][i+1:]
        url = BASE_IMAGE_URL + mvCode
    except:
        pass

    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        try:
            img = soup.find("img")
            img_src = img.get("src")
        except:
            pass
    for movie in movies:
        if movie['fields']['movieCd'] == movie_data:
            movie['fields']['image'] = img_src

with open('movie.json', 'w',  encoding = 'utf-8') as make_file:
    json.dump(movies, make_file, ensure_ascii=False, indent="\t")