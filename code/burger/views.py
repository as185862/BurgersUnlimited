from django.shortcuts import render

# Create your views here.

import http.client
import requests
from requests.auth import HTTPBasicAuth
from  django.http import HttpResponse
import config
import auxMethods


def index(request):

    return render(request,'index.html')



def findRestaurant(request):


    address = request.POST['address']
    radius = int(request.POST['radius'])

    coordinates = auxMethods.geoCodeAddress(address)
    results  = auxMethods.findResturantsInRange(coordinates,radius)

    context = {'address': address , "radius" : radius , 'coordinates' : coordinates, 'results' : results}

    return render(request,'findRestaurant.html', context)


def midtownMenu(request):

    return render(request,'midtownMenu.html')

def southlandMenu(request):

    return render(request,'southlandMenu.html')

def highlandsMenu(request):

    return render(request,'highlandsMenu.html')