from flask import Blueprint, render_template, request, jsonify, make_response
import json
from PIL import Image
import  urllib
from random import randint
from urllib.request import urlopen
page = 1
baseUrl = "https://api.themoviedb.org/3/discover/movie?api_key=31657fcbc4dc6a9f0e0277b60a6314e9&language=en-US&pg=2&sort_by=popularity.desc&with_genres="
tempUrl = ""
tempUrl = baseUrl + str(page)
runningUrl = ""
json_obj = urlopen(baseUrl)
data = json.load(json_obj)
var = data['results']
list_len = len(data['results'])

dontWatch = []
watch = []

i = 0
constantString = ""

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    return render_template("index.html")

@views.route('/setGenres', methods=['GET','POST'])
def setGenres():
    global constantString
    global baseUrl
    global i
    global json_obj
    global data
    global page
    global var
    global runningUrl
    global page
    req = request.get_json()
    print(req['genreString'])

    tempUrl = ""
    runningUrl = baseUrl + req['genreString'] + "&page="
    tempUrl = baseUrl + req['genreString'] + "&page=" + str(page)

    print(tempUrl)

    i = 0
    json_obj = urlopen(tempUrl)
    data = json.load(json_obj)
    var = data['results']
    list_len = len(data['results'])
    res = make_response(jsonify({"message": "JSON recieved", "title":var[i]['title'],"rating":var[i]['vote_average'],"description":var[i]['overview'],"poster":var[i]['poster_path']},200))
    return res

@views.route('/dontWatch', methods=['GET','POST'])
def dont_Watch():
    req = request.get_json()
    global constantString
    global baseUrl
    global i
    global json_obj
    global data
    global page
    global var
    print(req)

    if var[i]['id'] in dontWatch:
        while var[i]['id'] in dontWatch:
            i+=1
    else:
        dontWatch.append(var[i]['id'])
        i+=1
    print(dontWatch)
    if i == 20:
        tempUrl = ""
        i = 0
        page +=1
        tempUrl = runningUrl + str(page)
        json_obj = urlopen(tempUrl)
        data = json.load(json_obj)
        var = data['results']
    print(i)
    print(var[i]['title'])
    res = make_response(jsonify({"message": "JSON recieved", "title":var[i]['title'],"rating":var[i]['vote_average'],"description":var[i]['overview'],"poster":var[i]['poster_path']},200))
    return res

@views.route('/Watch', methods=['GET','POST'])
def will_Watch():
    req = request.get_json()
    global constantString
    global baseUrl
    global i
    global json_obj
    global data
    global page
    global var
    print(req)

    if var[i]['id'] in dontWatch:
        while var[i]['id'] in dontWatch:
            i+=1
    else:
        watch.append(var[i]['id'])
        i+=1
    print(watch)
    if i == 20:
        tempUrl = ""
        i = 0
        page +=1
        tempUrl = runningUrl + str(page)
        json_obj = urlopen(tempUrl)
        data = json.load(json_obj)
        var = data['results']
    print(i)
    print(var[i]['title'])
    res = make_response(jsonify({"message": "JSON recieved", "title":var[i]['title'],"rating":var[i]['vote_average'],"description":var[i]['overview'],"poster":var[i]['poster_path']},200))
    return res


