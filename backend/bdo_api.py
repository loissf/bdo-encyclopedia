import requests
import json

from file_functions import openJSON, createJSON
from Item import ListItem, SubListItem, HotListItem, ItemOrders

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
        "searchResult": ",".join(search[:100])
    }

    response = requests.request('POST', url, json=payload, headers=headers)
    attributeList = __responseToAttributes(response.text)
    items = __mapSearchListItem(attributeList)
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
    attributeList = __responseToAttributes(response.text)
    items = __mapSubListItem(attributeList)
    return items


def getBiddingInfo(id: int, enhancement: int) -> list[ItemOrders]:
    url = 'https://eu-trade.naeu.playblackdesert.com/Trademarket/GetBiddingInfoList'
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "BlackDesert"
    }
    payload = {
        "keyType": 0,
        "mainKey": id,
        "subKey": enhancement
    }

    response = requests.request('POST', url, json=payload, headers=headers)
    attributeList = __responseToAttributes(unpack(response.content))
    items = __mapItemOrders(attributeList)
    return items


def getPriceInfo(id: int, enhancement: int) -> list[ItemOrders]:
    url = 'https://eu-trade.naeu.playblackdesert.com/Trademarket/GetMarketPriceInfo'
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "BlackDesert"
    }
    payload = {
        "keyType": 0,
        "mainKey": id,
        "subKey": enhancement
    }

    response = requests.request('POST', url, json=payload, headers=headers)
    prices = __responseToValues(response.text)
    return prices


def __getResultMsg(msg: str):
    try:
        dictionary = json.loads(msg)
        result = dictionary['resultMsg']
    except:
        result = msg
    

    if(result[-1] == "|"):
        result = result[:-1]

    return result


def __responseToAttributes(response):
    values = []

    result = __getResultMsg(response)

    splitted = result.split("|")

    for item in splitted:
        attributes = item.split("-")
        values.append(attributes)
    
    return values


def __responseToValues(response):
    values = []

    result = __getResultMsg(response)

    splitted = result.split("-")

    for value in splitted:
        values.append(int(value))
    
    return values


def __mapSearchListItem(attributeList):
    items = []
    for attributes in attributeList:
        
        try:
            dictionaryEntry = dictionary.get(str(attributes[0]))
            item = ListItem(
                id = int(attributes[0]),
                name = dictionaryEntry['name'],
                grade = int(dictionaryEntry['grade']),
                stock = int(attributes[1]),
                basePrice = int(attributes[2]),
                totalTrades = int(attributes[3]),
                icon = f"https:\\cdn.arsha.io/icons/{attributes[0]}.png",
            )

            items.append(item)

        except Exception as e:
            print(e)
            print(f"Error getting item {attributes[0]}")
    return items


def __mapListItem(attributeList):
    items = []
    for attributes in attributeList:
        
        try:
            dictionaryEntry = dictionary.get(str(attributes[0]))
            item = ListItem(
                id = int(attributes[0]),
                name = dictionaryEntry['name'],
                grade = int(dictionaryEntry['grade']),
                stock = int(attributes[1]),
                totalTrades = int(attributes[2]),
                basePrice = int(attributes[3]),
                icon = f"https:\\cdn.arsha.io/icons/{attributes[0]}.png",
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
                id = int(attributes[0]),
                name = dictionaryEntry['name'],
                grade = int(dictionaryEntry['grade']),
                enhancement = int(attributes[1]),
                basePrice = int(attributes[3]),
                stock = int(attributes[4]),
                totalTrades = int(attributes[5]),
                lastPrice = int(attributes[8]),
                lastSale = int(attributes[9]),
                icon = f"https:\\cdn.arsha.io/icons/{attributes[0]}.png",
                mainCategory = int(dictionaryEntry['main_category']),
                subCategory = int(dictionaryEntry['sub_category'])
            )

            items.append(item)

        except Exception as e:
            print(e)
            print(f"Error getting item {attributes[0]}")
    return items


def __mapItemOrders(attributeList):
    orders = []
    for attributes in attributeList:

        sellOrders = int(attributes[1])
        buyOrders = int(attributes[2])

        order = ItemOrders(
            price = int(attributes[0]),
            orders = sellOrders if sellOrders > 0 else buyOrders,
            sell = sellOrders > 0
        )

        orders.append(order)
    return orders