import requests
from pprint import pprint
from decouple import config  # .env에 KEY 저장
from datetime import datetime, timedelta
import json
BASE_URL_MAKER = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
BASE_URL_MINFO = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
KEY = config('KEY')


# 요청보내기

# response = requests.get(API_URL_NAVER, headers=HEADERS).json()


Boxoffice_List_50W = {}

for i in range(50, 0, -1):
    week_del = i

    targetDt = datetime.today() - timedelta(weeks = week_del) #해당일로 부터 2주를 빼겠다.
    targetDt = targetDt.strftime('%Y%m%d')
    API_URL_MAKER = f'{BASE_URL_MAKER}?key={KEY}&targetDt={targetDt}'
    response = requests.get(API_URL_MAKER)
    data = response.json()
    print(data)
    for rank in range(10):
        need_data = {}
        need_data['title'] = data['boxOfficeResult']['weeklyBoxOfficeList'][rank]['movieNm']
        need_data['movieCd'] = data['boxOfficeResult']['weeklyBoxOfficeList'][rank]['movieCd']
        need_data['audiAcc'] = data['boxOfficeResult']['weeklyBoxOfficeList'][rank]['audiAcc']
        need_data['openDt'] = data['boxOfficeResult']['weeklyBoxOfficeList'][rank]['openDt']
        need_data['pubdate'] = need_data['openDt'][0:4]
        Boxoffice_List_50W[data['boxOfficeResult']['weeklyBoxOfficeList'][rank]['movieCd']] = need_data


# 장르
for code in Boxoffice_List_50W:
    Boxoffice_List_50W[code]['genres'] = []
    Boxoffice_List_50W[code]['directors'] = []
    Boxoffice_List_50W[code]['actors'] = []
    api_url = f'{BASE_URL_MINFO}?key={KEY}&movieCd={code}'

    response = requests.get(api_url)
    data = response.json()
    for a in data['movieInfoResult']['movieInfo']['genres']:
        Boxoffice_List_50W[code]['genres'].append(a['genreNm'])

    for a in data['movieInfoResult']['movieInfo']['directors']:
        Boxoffice_List_50W[code]['directors'].append(a['peopleNm'])
    
    cnt = 0
    for a in data['movieInfoResult']['movieInfo']['actors']:
        Boxoffice_List_50W[code]['actors'].append(a['peopleNm'])
        cnt += 1
        if cnt == 3:
            break

with open('movies.json', 'w',  encoding = 'utf-8') as make_file:
    json.dump(Boxoffice_List_50W, make_file, ensure_ascii=False, indent="\t")
