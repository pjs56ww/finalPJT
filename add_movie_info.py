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
    idx = 0
    for i in range(len(data['items'])):
        flag = False
        if len(data) == 1:  # 검색한 영화 결과가 1 일 경우
            idx = 0 # [0]번 인덱스 값을 바로 movie 변수에 저장
        else:
            for i in range(len(data['items'])):  # 검색 결과가 여러 개인 경우 (동명의 영화가 2개 이상)
                if len(movie_datas[movie_data]['directors']) != 0:
                    for directorNm in movie_datas[movie_data]['directors'][0].split():
                        # 감독이 여러명인 경우에 [0]번 인덱스만 비교
                        # 외국인 감독의 경우 영진위와 네이버의 표기가 다른 경우 존재하므로
                        # 띄어쓰기를 기준으로 이름을 나누어 비교
                        # ex) 영진위 제공 '데이빗 야로베스키' / 네이버 제공 '데이비드 야로베스키'
                        # => 데이빗 / 야로베스키 로 나누어
                        # => if   '데이빗'  in '데이비드 야로베스키'
                        # => if '야로베스키' in '데이비드 야로베스키' 식으로 비교
                        if directorNm in data['items'][i].get('director'):  # 감독명.split() 중 같은 결과가 있다면
                            idx = i  # movie 변수에 해당 결과를 저장한 뒤 break
                            break
    
            

    if len(data['items']) >= 1:
        # 줄거리
        paragraph_data_header = ""
        paragraph_data_body = ""

        with urllib.request.urlopen(data['items'][idx]['link']) as response:
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
        movie_datas[movie_data]['image'] = data['items'][idx]['image']


        # 점수
        movie_datas[movie_data]['score'] = data['items'][idx]['userRating']

    else:
        print(movie_data)
      

with open('movies_final.json', 'w',  encoding = 'utf-8') as make_file:
    json.dump(movie_datas, make_file, ensure_ascii=False, indent="\t")