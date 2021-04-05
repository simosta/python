import requests
import json
def get_movies_from_tastedive(mov):#gets a dictionary from search
    baseurl='https://tastedive.com/api/similar'
    search={}
    search["q"]=mov
    search["limit"]="5"
    search["type"]="movies"
    results = requests.get(baseurl, params=search)
    dict=results.json()
    return dict
# print(get_movies_from_tastedive('Black Panther'))

def extract_movie_titles (dict):#list of 5 titles
    titles=[d["Name"] for d in dict["Similar"]["Results"]]
    return titles

def get_related_titles (lst):#take a list of movies and make one recommendation list without repetition
    allin=[]
    for each in lst:
        dict=get_movies_from_tastedive(each)
        titles=extract_movie_titles(dict)
        for title in titles:
            if title not in allin:
                allin.append(title)
    return allin
# we move from tastedive to omdb
def get_movie_data(mov):#find a movie in a database
    baseurl='http://www.omdbapi.com/'
    search={}
    search["t"]=mov
    search["r"]='json'
    results = requests_with_caching.get(baseurl, params=search)
    dict=results.json()
    return dict

def get_movie_rating(dict):#gives rating as integer
    rlist=dict["Ratings"]
    for each in rlist:
        if each["Source"]=="Rotten Tomatoes":
            value=each["Value"].strip('%')
            return int(value)
    return 0

def get_sorted_recommendations(movlist):#need to sort the list by rating 100 to zero and
    ratings={}
    recs=get_related_titles(movlist)
    for rec in recs:
        dict=get_movie_data(rec)
        rating=get_movie_rating(dict)
        ratings[rec]=rating
    y=sorted(ratings.keys(), key = lambda k: -ratings[k]) #this breaks ties in sorting in abcd instead of dcba if I was using reverse=True
    return y
