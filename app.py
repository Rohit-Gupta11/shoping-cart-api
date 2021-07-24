from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from bson import ObjectId
import json
import uuid

# Initializing the flask app
app = Flask(__name__)

# MongoDB setup
MONGO_URI = '<YOUR MONGO DB CONNECTION STRING>'

cluster = MongoClient(MONGO_URI)
db  = cluster["testingDB"]
collection = db["carts"]

# home route
@app.route("/")
def home():
    return "<h1>Welcome to shoping cart</h1>"

# create a new cart
@app.route("/cart/create", methods=["POST"])
def create_cart():
    if request.method == "POST":
        data = {'items':[], 'totalItems': 0}
        new_cart_id = str(collection.insert_one(data).inserted_id)
        return jsonify({
            'cartId': new_cart_id,
            'status': 'created'})
    else:
        return jsonify('something wents wrong')

# view an existing cart
@app.route("/cart/<cartId>", methods=["GET"])
def view_cart(id):
    cart = collection.find_one({"_id": ObjectId(cartId)})    
    
    if cart and request.method == "GET":
        data = json.loads(dumps(cart))
        return data
    else:
        return jsonify({"message": "cart does not exist"})

# get items from cart
@app.route("/cart/<cartId>/items", methods=["GET"])
def get_items(cartId, itemId):
    cart = collection.find_one({"_id": ObjectId(id)})
    
    if cart and request.method == "GET":
        data = json.loads(dumps(cart))
        return jsonify({'items':data['items']})
    
    else:
        return jsonify({"message": "cart does not exist"})

# add items in cart
@app.route("/cart/<cartId>/add", methods=["PUT"])
def add_items(cartId):
    cart = collection.find_one({"_id": ObjectId(cartId)})
    
    if cart and request.method == "PUT":
        data = json.loads(dumps(cart))
        req_body = request.json
        
        data['items'].append({
            "itemId": data['totalItems'] + 1,
            "name": req_body['name'],
            "category": req_body['category'],
            "price": req_body['price']
        })

        updated_items = data['items']
        updated_totalItems = data['totalItems'] = len(data['items'])
        
        collection.update_one(
            {"_id": ObjectId(cartId)},
            {"$set": {
                "items": updated_items, 
                "totalItems": updated_totalItems 
            } 
        })

        return data
    
    else:
        return jsonify({"message" : "cart does not exist"})

# remove items from cart
@app.route("/cart/<cartId>/remove/<int:itemId>", methods=["DELETE"])
def remove_items(cartId, itemId):
    cart = collection.find_one({"_id": ObjectId(cartId)})

    if cart and request.method == "DELETE":
        data = json.loads(dumps(cart))

        for item in data['items']:
            if item['itemId'] == itemId:
                data['items'].remove(item)
                collection.update_one(
                    {"_id": ObjectId(cartId)},
                    {"$set": {
                        "items": data['items'], 
                        "totalItems": len(data['items']) 
                    } 
                })
                return jsonify({"message": "success"})
            else:
                return jsonify({"message": "item does not found"})
    else:
        return jsonify({"message": "cart does not exist"})

if __name__ == "__main__":
    app.run(debug=True)