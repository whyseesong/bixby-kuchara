from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse

from .serializers import MovieSchuduleSerializer
from .serializers import TheaterSerializer
from .serializers import MovieSerializer
from .serializers import NamedPointStructresSerializer

from .models import MovieSchedules
from .models import Movies
from .models import Theaters
from .models import NamedPointStructres

from .crawling import crawl

import math
import numbers
import json


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class TheaterViewSet(viewsets.ModelViewSet):
    queryset = Theaters.objects.all()
    serializer_class = TheaterSerializer

class MovieScheduleViewSet(viewsets.ModelViewSet):
    queryset = MovieSchedules.objects.all()
    serializer_class = MovieSchuduleSerializer

class NamedPointStructureViewSet(viewsets.ModelViewSet):
    queryset = NamedPointStructres.objects.all()
    serializer_class = NamedPointStructresSerializer
    

def get_euclidean_distance(x1, y1, x2, y2, round_decimal_digits=6):
    if x1 is None or y1 is None or x2 is None or y2 is None:
        return None
    
    dlong = abs(x2-x1)
    if dlong >= 180:
        dlong -= 360
    dlat = y2 - y1

    return round(math.sqrt(pow(dlong, 2)+pow(dlat, 2)), round_decimal_digits)


theaterFlag = {
    'name':'경희대',
    'point': {
        'latitude':12.124,
        'longitude':32.154
    }
}

movieScheduleFlag = {
    'subtitle': True,        
    'dubbing': False,               
    'digitalized': True,           
    'lateNight': False,   
    'morning': False,
}

theater = {
    'theaterName': '',
    'theaterCode':'',
    'regionCode':'',
    'brand':'',
    'theaterFlag': theaterFlag
}

movie = {
    'movieName':'',
    'duration':'',
    'movieRating':'',
    'director':'',
    'actors':'',
    'genre':''
}

movieSchedule = {
    'movie': movie,
    'totalSeat':'',
    'availableSeat':'',
    'theater': theater,
    'movieScheduleFlag':movieScheduleFlag,
    'room':'',
}


def SearchWithPos(request):
    movieJson = ""
    try:
        longitude = float(request.GET['longitude'])
    except:
        longitude = 0.0
    
    try:
        latitude = float(request.GET['latitude'])
    except:
        latitude = 0.0

    print('long:{}, lat:{}'.format(latitude, longitude))

    allTheater = Theaters.objects.all()
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        print("Dist {}".format(dist))
        if dist < 0.1:
            movie_info = crawl(reqtheater.regionCode, reqtheater.theaterCode)
            print(movie_info)
            print(type(movie_info['movieName']))
            print('[DEBUG]: ' + movie_info['movieName'])
            movie['movieName'] = movie_info['movieName']
            print('[DEBUG]: ' + movie_info['movieName'])
            movie['movieRating'] = movie_info['movieRating']
            
            theater['theaterName'] = reqtheater.theaterName
            theater['theaterCode'] = reqtheater.theaterCode
            theater['regionCode'] = reqtheater.regionCode
            theater['brand'] = reqtheater.brand

            movieSchedule['room'] = movie_info['room']
            movieSchedule['totalSeat'] = movie_info['seatInfo']
            movieSchedule['availableSeat'] = movie_info['seatInfo']
            movieSchedule['movie'] = movie
            movieSchedule['theater'] = theater            

            movieJson += json.dumps(movieSchedule, ensure_ascii=False)

    return JsonResponse(movieJson, safe=False)



def movie_list(request):
   
    json_res = dict()
    try:
        theaterName = request.GET['theaterName']
    except:
        theaterName = "조커"

    
    reqTheater = Theaters.objects.get(theaterName=theaterName)
    # reqMovies = MovieSchedules.objects.filter(theater=reqTheater.id)
    
    movieinfo = crawl(reqTheater.regionCode, reqTheater.theaterCode)
    '''
    print(movieinfo)

    for reqMovie in reqMovies:
        print(reqMovie.room)
        
    print(reqTheater.theaterName)
'''
    return JsonResponse(movieinfo, safe=False)
'''
    return JsonResponse({
        'message':'안녕 파이썬 장고',
        'items' : ['python', 'django']
    })
'''
# Create your views here.
