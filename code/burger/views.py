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




    context = {'address': address , "radius" : radius , 'coordinates' : coordinates}


    # How to insert separate method for geocoding?






    return render(request,'findRestaurant.html', context)