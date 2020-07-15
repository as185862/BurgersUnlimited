import requests
import config


def createItem(itemName, version, shortDescription):
    url = 'https://gateway-staging.ncrcloud.com/catalog/items/%s'%itemName

    headers = {
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708',



    }

    # version --> description -->
    payload = "{\"version\":%s,\"shortDescription\":{\"values\":[{\"locale\":\"en-US\",\"value\":\"%s\"}]},\"status\":\"ACTIVE\"}" %(version,shortDescription)
    temp = "{\"version\":88,\"linkGroupType\":\"DEPOSIT\",\"shortDescription\":{\"values\":[{\"locale\":\"en-US\",\"value\":\"sample text\"}]},\"tag\":\"substitutes\",\"status\":\"INACTIVE\",\"restriction\":{\"maxQuantity\":88,\"minQuantity\":83,\"freeQuantity\":23,\"defaultQuantity\":68,\"visibilityScope\":\"INTERNAL\"},\"linkItems\":[],\"substitutionGroup\":{\"linkGroupCode\":\"29837289\"},\"posNumber\":\"String\",\"dynamicAttributes\":[]}"


    example = "{\"version\":88," \
              "\"linkGroupType\":\"DEPOSIT\"," \
              "\"description\":{\"values\":[{\"locale\":\"en-US\"," \
              "\"value\":\"sample text\"}]}," \
              "\"tag\":\"substitutes\"," \
              "\"status\":\"INACTIVE\"," \
              "\"restriction\":{\"maxQuantity\":88," \
              "\"minQuantity\":83," \
              "\"freeQuantity\":23," \
              "\"defaultQuantity\":68," \
              "\"visibilityScope\":\"INTERNAL\"}," \
              "\"linkItems\":[]," \
              "\"substitutionGroup\":{\"linkGroupCode\":\"29837289\"}," \
              "\"posNumber\":\"String\"," \
              "\"dynamicAttributes\":[]}"

    r = requests.put(url, payload, auth=(config.USER, config.PASSWORD), headers=headers)
    print(r.json())

name = 'Hamburger Deluxe'
version = 1.0
description = "A 1/4 burger grilled to perfection, adorned with lettuce, tomato, onion, and mayonnaise."




createItem(name,version,description)



