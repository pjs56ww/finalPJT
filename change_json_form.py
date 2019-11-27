import requests
from pprint import pprint
from decouple import config  # .env에 ID, SECRET 저장
from datetime import datetime, timedelta
import json


with open('movies_final.json', 'r', encoding='utf-8') as f:
    movie_datas = json.load(f)

genre = []
actor = []
director = []
movie = []


for movie_data in movie_datas:
    a = {
        "model": "movies.movie",
        "pk": len(movie) + 1,
        "fields": {
            'movieCd': '', 
            'title': '',
            'description': '',
            'image': '',
            'openDt': '',
            'audiAcc': '',
            'score': '',
            'directors': [],
            'actors': [],
            'genres': [],
        }
        }
    a["fields"]["movieCd"] = movie_datas[movie_data]["movieCd"]
    a["fields"]["title"] = movie_datas[movie_data]["title"]
    if movie_datas[movie_data]["description"][0] == 0:
        a["fields"]["description"] = movie_datas[movie_data]["description"][0] + '\r' + movie_datas[movie_data]["description"][1]
    else:
        a["fields"]["description"] = movie_datas[movie_data]["description"][1]
    a["fields"]["image"] = movie_datas[movie_data]["image"]
    a["fields"]["openDt"] = movie_datas[movie_data]["openDt"]
    a["fields"]["audiAcc"] = movie_datas[movie_data]["audiAcc"]
    a["fields"]["score"] = movie_datas[movie_data]["score"]
    
    # 감독이 감독 DB에 존재하는지 확인 후 없으면 추가
    for  direc in movie_datas[movie_data]["directors"]:
        flag = 0
        for i in range(len(director)):
            if director[i]['fields']['name'] == direc:
                flag = 1
                a["fields"]["directors"].append(director[i]['pk'])
                break
        if flag == 0:
            b = {
                "model": "movies.director",
                "pk": len(director) + 1,
                "fields": {
                    "name": direc
                }
            }
            director.append(b)
            a["fields"]["directors"].append(len(director))

    # 배우가 배우 DB에 존재하는지 확인 후 없으면 추가
    for  act in movie_datas[movie_data]["actors"]:
        flag = 0
        for i in range(len(actor)):
            if actor[i]['fields']['name'] == act:
                flag = 1
                a["fields"]["actors"].append(actor[i]['pk'])
                break
        if flag == 0:
            b = {
                "model": "movies.actor",
                "pk": len(actor) + 1,
                "fields": {
                    "name": act
                }
            }
            actor.append(b)
            a["fields"]["actors"].append(len(actor))

    # 장르가 장르 DB에 존재하는지 확인 후 없으면 추가
    for  gen in movie_datas[movie_data]["genres"]:
        flag = 0
        for i in range(len(genre)):
            if genre[i]['fields']['genreNm'] == gen:
                flag = 1
                a["fields"]["genres"].append(genre[i]['pk'])
                break
        if flag == 0:
            b = {
                "model": "movies.genre",
                "pk": len(genre) + 1,
                "fields": {
                    "genreNm": gen
                }
            }
            genre.append(b)
            a["fields"]["genres"].append(len(genre))
    movie.append(a)

print(movie)

with open('director.json', 'w',  encoding = 'utf-8') as make_file:
    json.dump(director, make_file, ensure_ascii=False, indent="\t")

with open('actor.json', 'w',  encoding = 'utf-8') as make_file:
    json.dump(actor, make_file, ensure_ascii=False, indent="\t")

with open('genre.json', 'w',  encoding = 'utf-8') as make_file:
    json.dump(genre, make_file, ensure_ascii=False, indent="\t")

with open('movie.json', 'w',  encoding = 'utf-8') as make_file:
    json.dump(movie, make_file, ensure_ascii=False, indent="\t")
