import requests

from file_functions import openJSON, createJSON
from Item import ListItem, SubListItem, HotListItem

from unpacker import unpack

# Dictionary to get the equivalent name from each id
dictionary = openJSON("items.json", "src/resources")

# Request a subcategory from its id and category id
def getMarketList(categoryId: int, subcategoryId: int) -> list[ListItem]:
    url = 'https://eu-trade.naeu.playblackdesert.com/Trademarket/GetWorldMarketList'
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "BlackDesert"
    }
    payload = {
        "keyType": 0,
        "mainCategory": categoryId,
        "subCategory": subcategoryId
    }

    response = requests.request('POST', url, json=payload, headers=headers)
    attributeList = __responseToAttributes(unpack(response.content))
    items = __mapListItem(attributeList)
    return items


# Request a list of item's data from the web market from a list of ids
def getSearchList(search: list[str]) -> list[ListItem]:
    url = 'https://eu-trade.naeu.playblackdesert.com/Trademarket/GetWorldMarketSearchList'
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "BlackDesert"
    }
    payload = {
        "searchResult": ",".join(search)
    }

    response = requests.request('POST', url, json=payload, headers=headers)
    attributeList = __responseToAttributes(response.text)
    items = __mapListItem(attributeList)
    return items
    

# Request an item's data to the web market from its unique id
def getSubList(id: int) -> list[SubListItem]:
    url = 'https://eu-trade.naeu.playblackdesert.com/Trademarket/GetWorldMarketSubList'
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "BlackDesert"
    }
    payload = {
        "keyType": 0,
        "mainKey": id
    }

    response = requests.request('POST', url, json=payload, headers=headers)
    attributeList = __subListResponseToAttributes(response.text)
    items = __mapSubListItem(attributeList)
    return items


def __responseToAttributes(response):
    itemList = []

    splitted = response.split("|")

    for item in splitted:
        attributes = item.split("-")
        itemList.append(attributes)
    
    return itemList[:-1]


def __subListResponseToAttributes(response):
    itemList = []

    splitted = response[29:][:-3].split("|")

    for item in splitted:
        attributes = item.split("-")
        itemList.append(attributes)
    
    return itemList[:-1]


def __mapListItem(attributeList):
    items = []
    for attributes in attributeList:
        
        try:
            dictionaryEntry = dictionary.get(str(attributes[0]))
            item = ListItem(
                id = attributes[0],
                name = dictionaryEntry['name'],
                grade = dictionaryEntry['grade'],
                stock = attributes[1],
                basePrice = attributes[2],
                totalTrades = attributes[3],
                icon = f"https:\\cdn.arsha.io/icons/{attributes[0]}.png"
            )

            items.append(item)

        except Exception as e:
            print(e)
            print(f"Error getting item {attributes[0]}")
    return items


def __mapSubListItem(attributeList):
    items = []
    for attributes in attributeList:
        
        try:
            dictionaryEntry = dictionary.get(str(attributes[0]))
            item = SubListItem(
                id = attributes[0],
                name = dictionaryEntry['name'],
                grade = dictionaryEntry['grade'],
                enhancement = attributes[1],
                basePrice = attributes[3],
                stock = attributes[4],
                totalTrades = attributes[5],
                lastPrice = attributes[8],
                lastSale = attributes[9],
                icon = f"https:\\cdn.arsha.io/icons/{attributes[0]}.png"
            )

            items.append(item)

        except Exception as e:
            print(e)
            print(f"Error getting item {attributes[0]}")
    return items