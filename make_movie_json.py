import requests
from pprint import pprint
from decouple import config  # .env에 KEY 저장
from datetime import datetime, timedelta
import json
BASE_URL_MAKER = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'

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
        Boxoffice_List_50W[data['boxOfficeResult']['weeklyBoxOfficeList'][rank]['movieCd']] = need_data


with open('movies.json', 'w',  encoding = 'utf-8') as make_file:
    json.dump(Boxoffice_List_50W, make_file, ensure_ascii=False, indent="\t")
