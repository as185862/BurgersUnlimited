import requests
import config

def createSite():
    url = 'https://gateway-staging.ncrcloud.com/site/sites'
    payload = "{\"id\":\"mbkm8lhlvz37we91\",\"siteName\":\"Burgers Unlimited Highlands\",\"enterpriseUnitName\":\"Burgers Unlimited\",\"hours\":[],\"contact\":{\"contactPerson\":\"James Burger\",\"phoneNumber\":\"4041231234\",\"phoneNumberCountryCode\":\"44\"},\"timeZone\":\"US/Eastern\",\"locked\":true,\"description\":\"The Highlands location of the award-winning burger chain Burgers Unlimited .\",\"currency\":\"USD\",\"address\":{\"city\":\"Atlanta\",\"country\":\"USA\",\"postalCode\":\"30308\",\"state\":\"GA\",\"street\":\"1234 Main Street\"},\"coordinates\":{\"latitude\":33.6817952,\"longitude\":-84.4239568},\"status\":\"ACTIVE\",\"parentEnterpriseUnitId\":\"String\",\"customAttributeSets\":[{\"attributes\":[{\"key\":\"key\",\"value\":\"value\"}],\"typeName\":\"String\"}],\"referenceId\":\"String\",\"dayparts\":[]}"

    headers = {
        'nep-correlation-id': 'ojrz4z940etr6a73',
        'nep-organization': config.NEP_ORGANIZATION,
    }

    r = requests.post(url,auth=(config.USER,config.PASSWORD),headers = headers)

    print(r)




def getSite():
    url = 'https://gateway-staging.ncrcloud.com/site/sites/mbkm8lhlvz37we91'

    headers = {
        'nep-correlation-id': 'ojrz4z940etr6a73',
        'nep-organization': config.NEP_ORGANIZATION,
    }

    r = requests.get(url,auth=(config.USER,config.PASSWORD),headers=headers)

    print(r)





