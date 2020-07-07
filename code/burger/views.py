from django.shortcuts import render

# Create your views here.

import http.client
import requests
from requests.auth import HTTPBasicAuth
from  django.http import HttpResponse
import config

def index (request):

    url = "https://gateway-staging.ncrcloud.com/site/sites/find-by-criteria?pageSize=1000"
    payload = "{\n\t\"criteria\": {\n\t\t\"siteName\": \"*0019*\",\n\t\t\"status\": \"ACTIVE\"\n\t}\n}"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'nep-correlation-id': 'ojrz4z940etr6a73',
        'nep-organization': config.NEP_ORGANIZATION,
        'nep-application-key': config.NEP_APPLICATION_KEY,
    }
    response = requests.request("POST", url, headers=headers, data=payload,auth=(config.USER,config.PASSWORD))
    print(response.text.encode('utf8'))
    return HttpResponse(response)

'''
   url = 'https://gateway-staging.ncrcloud.com/site/sites'
   payload = "{\"id\":\"mbkm8lhlvz37we91\",\"siteName\":\"Burgers Unlimited Highlands\",\"enterpriseUnitName\":\"Burgers Unlimited\",\"hours\":[],\"contact\":{\"contactPerson\":\"James Burger\",\"phoneNumber\":\"4041231234\",\"phoneNumberCountryCode\":\"44\"},\"timeZone\":\"US/Eastern\",\"locked\":true,\"description\":\"The Highlands location of the award-winning burger chain Burgers Unlimited .\",\"currency\":\"USD\",\"address\":{\"city\":\"Atlanta\",\"country\":\"USA\",\"postalCode\":\"30308\",\"state\":\"GA\",\"street\":\"1234 Main Street\"},\"coordinates\":{\"latitude\":33.6817952,\"longitude\":-84.4239568},\"status\":\"ACTIVE\",\"parentEnterpriseUnitId\":\"String\",\"customAttributeSets\":[{\"attributes\":[{\"key\":\"key\",\"value\":\"value\"}],\"typeName\":\"String\"}],\"referenceId\":\"String\",\"dayparts\":[]}"
   #payload = "{\"id\":\"a6c0b9c5ed4c40f8bf584dca562b47eb\",\"siteName\":\"NCR's World Headquarters\",\"enterpriseUnitName\":\"NCR World Headquarters\",\"hours\":[],\"contact\":{\"contactPerson\":\"George Burdell\",\"phoneNumber\":\"6787323274\",\"phoneNumberCountryCode\":\"44\"},\"timeZone\":\"US/Eastern\",\"locked\":true,\"description\":\"A state-of-the-art campus designed to attract top talent, showcase NCRs technology solutions and serve as an iconic landmark for the City of Atlanta.\",\"currency\":\"USD\",\"address\":{\"city\":\"Atlanta\",\"country\":\"USA\",\"postalCode\":\"30308\",\"state\":\"GA\",\"street\":\"860 Spring St. NW\"},\"coordinates\":{\"latitude\":33.6817952,\"longitude\":-84.4239568},\"status\":\"ACTIVE\",\"parentEnterpriseUnitId\":\"a6c0b9c5ed4c40f8bf584dcb562b47eb\",\"customAttributeSets\":[{\"attributes\":[{\"key\":\"key\",\"value\":\"value\"}],\"typeName\":\"String\"}],\"referenceId\":\"String\",\"dayparts\":[]}"

   headers = {
       'nep-correlation-id': 'ojrz4z940etr6a73',
       'nep-organization': config.NEP_ORGANIZATION,
       'nep-application-key': config.NEP_APPLICATION_KEY,
   }

   r = requests.post(url, payload, auth=(config.USER, config.PASSWORD), headers=headers)

   print(r)
   
   return HttpResponse(r)




    url = "https://gateway-staging.ncrcloud.com/provisioning/user-profiles"

    headers={

            'accept': 'application/json',
            'nep-application-key': config.NEP_APPLICATION_KEY,
    }
    r = requests.get(url,auth=(config.USER, config.PASSWORD), headers = headers)

    print(r.text)
    return HttpResponse(r)

'''