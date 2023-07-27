import time
from file_functions import openJSON, createJSON

cachePath = "backend/api-cache"

def createCache(key: list[any], data: any) -> None:
    stringKey = "-".join(map(str,key))
    currentTimestamp = time.time()

    cache = {
        "key": stringKey,
        "timestamp": currentTimestamp,
        "data": data,
    }
    createJSON(cache, f"{stringKey}.json", cachePath)

data = {
    "completelyDifferentStuff": "stuff",
    "moreStuff": "value",
}

def readCache(key: list[any]) -> dict[str, any]:
    stringKey = "-".join(map(str,key))
    currentTimestamp = time.time()
    
    return openJSON(f"{stringKey}.json", cachePath)

def checkCache(key: list[any]):
    cache = readCache(key)

    if(not cache):
        return None
    
    timeDelta = time.time() - cache['timestamp']

    # timestamp in seconds 900 seconds = 15 mins
    if(timeDelta > 900):
        return None

    return cache['data']