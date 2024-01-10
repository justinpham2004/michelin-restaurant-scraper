import requests
from lxml import html
import excel_transfer

def allRestaurantData(url):
    restaurants = getRestaurants(url = url)
    # webbrowser.open('https://guide.michelin.com' + restaurants[1])
    count = 3
    #tokyo = excel_transfer.createSpreadsheet("tokyo")
    spreadsheet = excel_transfer.createSpreadsheet("city_restaurants")

    for restaurant in restaurants:
        restaurant_data = getRestaurantData('https://guide.michelin.com' + restaurant)
        excel_transfer.inputDataIntoSpreadsheet(spreadsheet, restaurant_data, count)
        count += 1

     

def getRestaurants(url): 
    res = requests.get(url)

    #print(res.status_code == requests.codes.ok)
    try:
            res.raise_for_status()
    except Exception as exc:
            print("There was a problem: %s" % (exc))

    tree = html.fromstring(res.content)

    return tree.xpath("//div/a[contains(@href, 'restaurant/')]/@href")



def getRestaurantData(url):
    data = dict(name = "", address = "", maplink = "", description = "")
    res = requests.get(url)

    #print(res.status_code == requests.codes.ok)
    try:
        res.raise_for_status()
    except Exception as exc:
        print("There was a problem: %s" % (exc))

    tree = html.fromstring(res.content)

    #PARSE AND ANALYZE DATA

    name =  tree.xpath('//h2[@class="restaurant-details__heading--title"]/text()') #print(name)
    data["name"] = name[0]
    
    
    short_des = tree.xpath('//li[@class="restaurant-details__heading-price"]/span[@class=""]/text()')[0].strip().replace("\n", "").replace(" ","")

    data["description"] = short_des
    
    address = tree.xpath('//li[@class="restaurant-details__heading--address"]/text()') #print(address)
    data["address"] = address[0]
    
    data["maplink"] = ('https://www.google.com/maps/place/' + address[0])
    #remember to parse address for district
    #description = tree.xpath("//div[@class='restaurant-details__description--text']/p/text()") #print(description)
    return data

