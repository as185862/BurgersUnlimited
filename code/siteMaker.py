import requests
import config



"""
Description: This function creates new sites on the NCR Platform
Parameters: (In Progress) A dictionary of the values that a user would like to be added to a new site
Returns: Nothing. (In Future) A Json confirming the creation of the site. Currently using print statements.

"""

def create(request):
    url = 'https://gateway-staging.ncrcloud.com/site/sites'

    headers = {
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708'
    }

    paylo1ad = "{\"id\":\"a6c0b9c5ed4c40f8\",\"siteName\":\"NCR's World Headquarters\",\"enterpriseUnitName\":\"NCR World Headquarters\",\"hours\":[],\"contact\":{\"contactPerson\":\"George Burdell\",\"phoneNumber\":\"6787323274\",\"phoneNumberCountryCode\":\"44\"},\"timeZone\":\"US/Eastern\",\"locked\":true,\"description\":\"A state-of-the-art campus designed to attract top talent, showcase NCRs technology solutions and serve as an iconic landmark for the City of Atlanta.\",\"currency\":\"USD\",\"address\":{\"city\":\"Atlanta\",\"country\":\"USA\",\"postalCode\":\"30308\",\"state\":\"GA\",\"street\":\"860 Spring St. NW\"},\"coordinates\":{\"latitude\":33.6817952,\"longitude\":-84.4239568},\"status\":\"ACTIVE\",\"parentEnterpriseUnitId\":\"a6c0b9c5ed4c40f8bf584dcb562b47eb\",\"customAttributeSets\":[{\"attributes\":[{\"key\":\"key\",\"value\":\"value\"}],\"typeName\":\"String\"}],\"referenceId\":\"String\",\"dayparts\":[]}"
    payload =  "{\"siteName\":\"Burgers Unlimited Southland\",\"enterpriseUnitName\":\"Burgers Unlimited Southland\",\"hours\":[],\"contact\":{\"contactPerson\":\"James Burgerman\",\"phoneNumber\":\"6787323274\",\"phoneNumberCountryCode\":\"44\"},\"timeZone\":\"US/Eastern\",\"locked\":true,\"description\":\"The Southland location of the award winning burger chain Burgers Unlimited.\",\"currency\":\"USD\",\"address\":{\"city\":\"Atlanta\",\"country\":\"USA\",\"postalCode\":\"30308\",\"state\":\"GA\",\"street\":\"860 Spring St. NW\"},\"coordinates\":{\"latitude\":33.6817952,\"longitude\":-84.4239568},\"status\":\"ACTIVE\",\"dayparts\":[]}"
    r = requests.post(url, payload, auth=(config.USER, config.PASSWORD), headers=headers)
    print (r)


"""
Description: This function allows a user to query the NCR Platform to locate a particular site,
Parameters: siteName 
Returns: Nothing. (In Future) A Json containing the information about the request statement. Currently using print statements.
"""

def query(locationName):
        url = 'https://gateway-staging.ncrcloud.com/site/sites/find-by-criteria?pageSize=10000'

        payload = "{\n\t\"criteria\": {\n\t\t\"siteName\": \"%s\",\n\t\t\"status\": \"ACTIVE\"\n\t}\n}" %locationName

        headers = {
            'content-type': 'application/json',
            'nep-organization': 'burgers-unlimited',
            'nep-correlation-id': '2020-0708'
        }

        r = requests.post(url, payload, auth=(config.USER, config.PASSWORD), headers=headers)
        print(r.json())


"""
Description: This function allows a user to update a particular site on the NCR Platform.
Parameters: id of the site 
Returns: Nothing. (In Future) A Json containing the information about the updated site. Currently using print statements.
"""


def update(id,name):
    url = url = 'https://gateway-staging.ncrcloud.com/site/sites/%s' %id

    payload = "{\"siteName\":\"%s\",\"enterpriseUnitName\":\"%s\",\"coordinates\":{\"latitude\":33.6407,\"longitude\":-84.4277},\"status\":\"ACTIVE\"}" %(name,name)

    headers ={
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708'
    }

    r = requests.put(url, payload, auth=(config.USER, config.PASSWORD), headers=headers)
    print(r.json())


    headers = {
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708'
    }


query("Burgers Unlimited Midtown")