from flask import Flask, jsonify, request, send_from_directory

from cache_functions import checkCache, createCache

from bdo_api import getSubList, getSearchList, getMarketList, getBiddingInfo, getPriceInfo

from enhancement_functions import getFsCost, getEnhancementChance, getItemEnhancementRange

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def test():
    return "<h1>Flask backend running<h1>"


@app.route('/items/<int:id>', methods = ['GET'])
def getItem(id: int):
    key = ['item', id]
    cache = checkCache(key)

    if(cache):
        return cache

    try:
        response = getSubList(id)
        items = []
        for item in response:
            items.append(item.__dict__)

        createCache(key, items)
        return items
    except Exception as e:
        print(e)
        return e.__str__()


# Item search does not use cache as there is unlimited search combinations
@app.route('/items', methods = ['GET'])
def getItemSearch():
    try:
        search = request.args.getlist("id")
        response = getSearchList(search)
        items = []
        for item in response:
            items.append(item.__dict__)
        return items
    except Exception as e:
        print(e)
        return e.__str__()


@app.route('/category/<int:category>/<int:subcategory>', methods = ['GET'])
def getCategory(category: int, subcategory: int):
    key = ['category', category, subcategory]
    cache = checkCache(key)

    if(cache):
        return cache

    try:
        response = getMarketList(category, subcategory)
        items = []
        for item in response:
            items.append(item.__dict__)

        createCache(key, items)
        return items
    except Exception as e:
        print(e)
        return e.__str__()


@app.route('/items/<int:id>/orders/<int:enhancement>', methods = ['GET'])
def getItemOrders(id: int, enhancement: int):
    key = ['orders', id, enhancement]
    cache = checkCache(key)

    if(cache):
        return cache

    try:
        response = getBiddingInfo(id, enhancement)
        orders = []
        for order in response:
            orders.append(order.__dict__)

        createCache(key, orders)
        return orders
    except Exception as e:
        print(e)
        return e.__str__()


@app.route('/items/<int:id>/price/<int:enhancement>', methods = ['GET'])
def getPriceHistory(id: int, enhancement: int):
    key = ['price', id, enhancement]
    cache = checkCache(key)

    if(cache):
        return cache

    try:
        prices = getPriceInfo(id, enhancement)
        createCache(key, prices)
        return prices
    except Exception as e:
        print(e)
        return e.__str__()


@app.route('/enhance/<int:id>/avaliable', methods = ['GET'])
def getAvaliableEnhancements(id: int):
    return getItemEnhancementRange(id)


@app.route('/enhance/<int:id>', methods = ['GET'])
def getItemEnhancementChance(id: int):
    try:
        lvl = int(request.args.get("lvl"))
        fs = int(request.args.get("fs"))
        return getEnhancementChance(id, lvl, fs).__str__() # Seems like, maybe, Flask doesnt like too long floats
    except Exception as e:
        print(e)
        return e.__str__()


@app.route('/enhance/fs', methods = ['GET'])
def getWhiteFsCost():
    try:
        amount = request.args.get("amount")
        return getFsCost(amount)
    except Exception as e:
        print(e)
        return e.__str__()


@app.route('/<path:filename>', methods=['GET', 'POST'])
def index(filename):
    filename = filename or 'index.html'
    if request.method == 'GET':
        return send_from_directory('.', filename)

    return jsonify(request.data)


if __name__ == "__main__":
    app.run(debug=True)