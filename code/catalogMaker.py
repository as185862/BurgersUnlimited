import requests
import config
import re

#TODO: Write method to call down price API results
#TODO: Combine price array and storeItem array
#TODO: Rewrite the menu call on the views page to filter name menu correctly
#TODO: Place temp menu on hmtl page :D

'''
Description: This function creates new items in the site catalog associated with the enterpriseId passed to this function. BEWARE: There is no delete function within the catalog API

Parameters: 
-itemName [ The name of the item that you want to create. NOTICE: Spaces are not allowed]
-version [ Which version of the itemName is this. NOTICE: When updating, you must increase this number]
-shortDescription [ A description of the itemName]
-location [ Which site(location) is this item being added to]
-department [ Which department within the site is this location going to]
-enterpriseId [ The alphanumeric id associated with the location. NOTICE: This was created when the site was created. If unknown use query() within siteMaker] 

Returns: N/A
'''


def createItem(itemName, version, shortDescription ,location, department, enterpriseId):
    url = 'https://gateway-staging.ncrcloud.com/catalog/items/%s' %(itemName)

    headers = {
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708',
        'nep-enterprise-id': '%s' % enterpriseId
    }

    payload = "{\"version\":%s,\"shortDescription\":{\"values\":[{\"locale\":\"en-US\",\"value\":\"%s\"}]},\"status\":\"ACTIVE\",\"merchandiseCategory\":\"%s\",\"departmentId\":\"%s\"}" %(version,shortDescription,location,department)

    r = requests.put(url, payload, auth=(config.USER, config.PASSWORD), headers=headers)
    print(r)


'''
Description: This function returns the item details of the itemName passed
Parameters: itemName [ name of the item you want information about]
Returns: Nothing right now ;p Under Construction
'''

def getItem(itemName):
    url = 'https://gateway-staging.ncrcloud.com/catalog/items/%s' %itemName
    headers = {
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708',
    }

    r = requests.get(url, auth=(config.USER,config.PASSWORD), headers = headers)
    print(r.json())


'''
Description:
Parameters:
Returns:
'''

def getStoreItems(storeName):
    url = 'https://gateway-staging.ncrcloud.com/catalog/items?merchandiseCategoryId=%s'%storeName
    headers = {
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708',
    }

    r = requests.get(url, auth=(config.USER, config.PASSWORD), headers=headers)
    tempItems = r.json()
    storeItems = []

    for item in tempItems['pageContent']:
        for nestedItem in item['itemId'].values():
            temp = nestedItem
            result = addSpacesInbetweenCaptialLetters(temp)
            storeItems.append(result)

    if storeName == 'BurgersUnlimitedMidtown':
        storeItems.remove('Hamburger Deleuxe')
    return storeItems

'''
Description:
Parameters:
Returns:
'''

def createPrice(itemName, itemPriceId, version, price):
    url = 'https://gateway-staging.ncrcloud.com/catalog/item-prices/%s/%s' % (itemName, itemPriceId)

    headers = {
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708',
        'nep-enterprise-unit':'a6c0b9c5ed4c40f8bf584dca562b47eb',
    }

    payload = "{\"version\":%s,\"price\":%s,\"currency\":\"US Dollar\",\"effectiveDate\":\"2020-07-16T18:22:05.784Z\",\"status\":\"ACTIVE\"}" %(version, price)
    r = requests.put(url,payload,auth=(config.USER,config.PASSWORD),headers=headers)

    print(r)

'''
Description:
Parameters:
Returns:
'''
def getPrice(itemName,itemPriceId,enterpriseId):
    url = 'https://gateway-staging.ncrcloud.com/catalog/item-prices/%s/%s' %(itemName, itemPriceId)
    headers = {
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708',
        'nep-enterprise-unit': '%s' %enterpriseId,

    }

    r = requests.get(url, auth=(config.USER, config.PASSWORD), headers=headers)
    print(r.json())

'''
Description:
Parameters:
Returns:
'''
#def getAllPrices(itemIds):

'''
Description:
Parameters:
Returns:
'''
def addSpacesInbetweenCaptialLetters(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)



'''
Description:
Parameters:
Returns:
'''




name = 'HamburgerDeluxe'
itemPriceId= '2'
version = 5.0
description = "A 1/4 lb burger grilled to perfection, adorned with lettuce, tomato, onion, and mayonnaise. "
location = "BurgersUnlimitedMidtown"
department = "Beef"
enterpriseId = config.Locations['Burgers Unlimited Midtown']


#createItem(name,version,description,location,department, enterpriseId)
#createPrice(name,itemPriceId,1,8)
#getPrice(name,itemPriceId,enterpriseId)

#getItem(name)

#getStoreItems('BurgersUnlimitedHighlands')


#createItem(name,version,description,location,department,enterpriseId)
#getItem("HamburgerDeluxe")


print(getStoreItems('BurgersUnlimitedMidtown'))




