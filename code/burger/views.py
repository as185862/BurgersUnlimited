from django.shortcuts import render

# Create your views here.

import http.client
import requests
from requests.auth import HTTPBasicAuth
from  django.http import HttpResponse
import config


def index(request):

    return render(request,'index.html')



def findRestaurant(request):

    print("Recived", request.GET , request.POST, request.body)


    return render(request,'findRestaurant.html')