from django.shortcuts import render

# Create your views here.

import http.client
import requests
from requests.auth import HTTPBasicAuth
from  django.http import HttpResponse
import config

def index (request):

    url = "https://gateway-staging.ncrcloud.com/provisioning/user-profiles"


    headers={

            'accept': 'application/json',
            'nep-application-key': config.NEP_APPLICATION_KEY,
        }
    r = requests.get(url,auth=(config.USER, config.PASSWORD), headers = headers)

    print(r.text)

    return HttpResponse(r)

