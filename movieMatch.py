import requests
import json
from urllib.request import urlopen

nameList = []
idList = []
urlG = 'https://api.themoviedb.org/3/genre/movie/list?api_key=31657fcbc4dc6a9f0e0277b60a6314e9&language=en-US'
json_objG = urlopen(urlG)
dataG = json.load(json_objG)
varG = dataG['genres']
list_lenG = len(dataG['genres'])
i = 0
while dataG['genres'] is not None:
    nameList.append(varG[i]['name'])
    idList.append(varG[i]['id'])
    i += 1
    if i == list_lenG:
        break


def getGenreID(genreName):
    return idList[nameList.index(genreName)]



userAnswer = ""
addingGenres = True
yesList = []
noList = []
genresList = []
visitedList = []
genreString = ""
if addingGenres:
    while True:
        if input("What you like to add another genre? : ") == "Yes":
            genreString += str(getGenreID(input("What Genres Would You Like To Watch? : "))) + ','
            #genresList.append(getGenreID(input("What Genres Would You Like To Watch? : ")))
        else:
            break
#url = 'https://api.themoviedb.org/3/movie/popular?api_key=31657fcbc4dc6a9f0e0277b60a6314e9&page='
url = "https://api.themoviedb.org/3/discover/movie?api_key=31657fcbc4dc6a9f0e0277b60a6314e9&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&with_genres={}%2C35&page=".format(genreString)
page = 1
urlT = url + str(page)
json_obj = urlopen(urlT)
data = json.load(json_obj)
i = 0
var = data['results']
list_len = len(data['results'])

while True:
    print("Choices : \n"
          "1 - Swipe \n"
          "2 - View Watch List \n"
          "3 - View Rejected List\n"
          "4 - Quit")
    choice = input("What would you like to do? ")
    if choice == "1":
        while data['results'] is not None:
            if var[i]['id'] not in visitedList:
                print("Would you like to watch \"" + var[i]['original_title'] + "\"?")
                print("Overview : " + var[i]['overview'])
                print("Rating : " + str(var[i]['vote_average']))
                print("Id : " + str(var[i]['id']))
                userAnswer = input("Yes or No? : ")
                if userAnswer == "1":
                    print("Added \"" + var[i]['original_title'] + "\" to the list")
                    yesList.append(var[i]['id'])
                    visitedList.append(var[i]['id'])

                elif userAnswer == "2":
                    print("\"" + var[i]['original_title'] + "\" will not be added to your list")
                    noList.append(var[i]['id'])
                    visitedList.append(var[i]['id'])
            i += 1
            print("\n")
            if i == list_len:
                if input("Continue? ") == 'yes':
                    page += 1
                    urlT = url + str(page)
                    json_obj = urlopen(urlT)
                    data = json.load(json_obj)
                    var = data['results']
                    list_len = len(data['results'])
                    i = 0
                else:
                    i = 0
                    break
    elif choice == "2":
        print(yesList)
    elif choice == "3":
        print(noList)
    elif choice == "4":
        break