import requests
import config
import re


#TODO: Write method to call down price API results
#TODO: Combine price array and storeItem array
#TODO: Rewrite the menu call on the views page to filter name menu correctly
#TODO: Place temp menu on hmtl page :D

HIGHLANDS = config.Locations['Burgers Unlimited Highlands']
SOUTHLAND = config.Locations['Burgers Unlimited Southland']
MIDTOWN = config.Locations ['Burgers Unlimited Midtown']

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

#FIXME: Have a sucess & failure message
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
    print(r.json)

'''
Description: This function returns the item details of the itemName passed
Parameters: itemName [name of the item you want information about]
Returns: returns the json of the item in question. If no results, returns nothing
'''

#FIXME: Have a return message to explain empty result
def getItem(itemName):
    url = 'https://gateway-staging.ncrcloud.com/catalog/items/%s' %itemName
    headers = {
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708',
    }

    r = requests.get(url, auth=(config.USER,config.PASSWORD), headers = headers)

    return r.json()

'''
Description: This function will call the catalog bulk getItem function. It will grab all the items associated with a  particular site/resturant 
Parameters: storeName [The name of the store you wish  to call  all the  items from]
Returns: An array with the names of all the items within the storeName.
'''

#FIXME: Have a message display if no results found
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
          #  storeItems.update({'name': nestedItem})
             name = nestedItem
             department = item['departmentId']
             result = {}
             result.update({'name':name, 'department':department})
             storeItems.append(result)


    #if storeName == 'BurgersUnlimitedMidtown':
       # storeItems.remove()

    # HACK: The  catalog api does not allow deletions. This is removing an error in the catalog
    for i in range(len(storeItems)):
        if storeItems[i]['name'] == "HamburgerDeleuxe":
            del storeItems[i]
            break
    return storeItems

'''
Description: This function creates a priceItem within the catalog API. The priceItem and item are tied together by the itemCode. I am using itemName as a replacement for itemCode

Parameters:
-itemName [The name that you entered for the item, when you made it]
-itemPriceId [ A unique id for the item. ]
-version [ Which version of the itemName is this. NOTICE: When updating, you must increase this number]
-price [How much the item will cost]
-enterpriseId [ The alphanumeric id associated with the location. NOTICE: This was created when the site was created. If unknown use query() within siteMaker] 

Returns: N/A
'''

#FIXME: Return a conformation or failure message
def createPrice(itemName, itemPriceId, version, price, enterpriseId):
    url = 'https://gateway-staging.ncrcloud.com/catalog/item-prices/%s/%s' % (itemName, itemPriceId)

    headers = {
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708',
        'nep-enterprise-unit': '%s' %enterpriseId
    }

    payload = "{\"version\":%s,\"price\":%s,\"currency\":\"US Dollar\",\"effectiveDate\":\"2020-07-16T18:22:05.784Z\",\"status\":\"ACTIVE\"}" %(version, price)
    r = requests.put(url,payload,auth=(config.USER,config.PASSWORD),headers=headers)

    print(r.json)

'''
Description: This function will find the priceItem from the associated itemName
Parameters:
-itemName [The name that you entered for the item, when you made it]
-itemPriceId [The itemPriceId you entered when you created the item]
-enterpriseId [ The alphanumeric id associated with the location. NOTICE: This was created when the site was created. If unknown use query() within siteMaker] 
Returns: A json of the priceItem from the requested itemName
'''
#FIXME: Write error message for priceItem not found
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
Description: This function will get all the priceItems from the given itemNames
Parameters:
itemIds [A list of itemNames]
-enterpriseId [ The alphanumeric id associated with the location. NOTICE: This was created when the site was created. If unknown use query() within siteMaker] 
Returns: A list of priceItems for the given itemNames
'''
def getAllPrices(itemIds,enterpriseId,):
    url = 'https://gateway-staging.ncrcloud.com/catalog/item-prices/get-multiple'
    headers = {
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708',
        'nep-enterprise-unit': '%s' % enterpriseId,
    }

    itemNames = []


    for i in range(len(itemIds)):
        #print(itemIds[i]['name'])
        itemNames.append(itemIds[i]['name'])

    modifiedItems  = createJsonString(itemNames)

    payload = "{\"itemIds\":[%s]}" %modifiedItems

    r = requests.post(url,payload, auth=(config.USER, config.PASSWORD),headers = headers)

    tempPrices = r.json()

    print(tempPrices)


    itemsWithPrices = []

    #print(tempPrices)

    #print(tempPrices['itemPrices'][0]['priceId']['itemCode'])
    #print(tempPrices['itemPrices'][0]['price'])





    i = 0
    for item in tempPrices['itemPrices']:
        result = {}
        price = item.get('price')
        nested = item.get('priceId')
        name = nested.get('itemCode')
        name = addSpacesInbetweenCaptialLetters(name)
        price = addChange(price)

        if isUnique(itemsWithPrices,name):
            result.update({'name': name, 'price': price, 'department': itemIds[i]['department']})
            itemsWithPrices.append(result)
            i += 1
        else:

            result.update({'name': name, 'price': price})


    '''    if name in itemsWithPrices.values():
            result.update({'name':name,'price':price})
        else:
            result.update({'name':name,'price':price, 'department':itemIds[i]['department']})
            itemsWithPrices.append(result)
            i += 1 '''


    return itemsWithPrices


'''
Description:
Parameters:
Returns:
'''
def addSpacesInbetweenCaptialLetters(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

'''
Description: A helper function to build json strings for the getPriceItems payload.
Parameters: items [A list of itemNames to be turned into a json string]
Returns: a string in the correct format for the getPriceItems payload.
'''

def createJsonString(items):
    String = ""

    for  item in items:
        String =  String + "{\"itemCode\":\"%s\"}," %item

    String =String.rstrip(',')

    return String


def isUnique(dict_list,item):
    for d in dict_list:
        if d['name'] == item:
            return False
    return True


def addChange(string):
    string = str(string)
    if "." not in string:
        string = string + '.00'
    return string

name = 'LargeDrink'
itemPriceId= '1'
version = 1
price = 2.25
description = "A 48oz fountain drink"
location = "BurgersUnlimitedSouthland"
department = "Drink"
enterpriseId = config.Locations['Burgers Unlimited Southland']

#createItem(name,version,description,location,department,enterpriseId)
#createPrice(name,itemPriceId,version,price,enterpriseId)
#print(getPrice(name,itemPriceId,enterpriseId))
#print(getItem(name))

#print(getPrice(name,itemPriceId,enterpriseId))

#print(getStoreItems("BurgersUnlimitedSouthland"))

midtownItems = getStoreItems("BurgersUnlimitedSouthland")
#print(getAllPrices(midtownItems,SOUTHLAND))
#print(getStoreItems("BurgersUnlimitedSouthland"))

#getPrice(name, itemPriceId, enterpriseId)

print(getAllPrices(midtownItems,SOUTHLAND))



