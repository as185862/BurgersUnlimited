from django.shortcuts import render

# Create your views here.

import http.client
import requests
from requests.auth import HTTPBasicAuth
from  django.http import HttpResponse
import config
import auxMethods
import catalogMaker

HIGHLANDS = config.Locations['Burgers Unlimited Highlands']
SOUTHLAND = config.Locations['Burgers Unlimited Southland']
MIDTOWN = config.Locations ['Burgers Unlimited Midtown']


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
    items = catalogMaker.getStoreItems('BurgersUnlimitedMidtown')
    items_prices = catalogMaker.getAllPrices(items,MIDTOWN)
    context = {'items':items_prices}

    return render(request,'midtownMenu.html',context)

def southlandMenu(request):

    items = catalogMaker.getStoreItems('BurgersUnlimitedSouthland')
    items_prices = catalogMaker.getAllPrices(items, SOUTHLAND)
    context = {'items': items_prices}

    return render(request, 'southlandMenu.html', context)

def highlandsMenu(request):
    items = catalogMaker.getStoreItems('BurgersUnlimitedHighlands')
    items_prices = catalogMaker.getAllPrices(items, HIGHLANDS)
    context = {'items': items_prices}

    return render(request, 'highlandsMenu.html', context)