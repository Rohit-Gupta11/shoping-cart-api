
# Shoping Cart API

## Tech Stack

***Python (Flask), MongoDB (PyMongo)***

  
## Installation
**1.** Clone the repository to your local computer.
```bash
  git clone https://github.com/Rohit-Gupta11/shoping-cart-api.git
  cd shoping-cart-api/
```

**2.** Create and activate virtual environment by running following in terminal.
```bash
  python -m venv venv
  venv\Scripts\activate
```

**3.** Install all the dependencies by running following in terminal.
```bash
  pip install -r requirements.txt
```

**4.** Now open app.py and assign your mongoDB connection string to MONGO_URI variable (i.e., line 11 in app.py)  
```bash
  MONGO_URI = '<YOUR MONGO DB CONNECTION STRING>'
```

**5.** Finally run the flask server.
```bash
  flask run
```

## Guide to use this API

All the endpoints of the API are given below:

**1.** First of all, create a cart, for creating cart make **POST** request to 
```bash
  /cart/create
```
A JSON response will recieve. Copy **cartId** for further process.

**2.** For viewing the cart(i.e., cartId), make **GET** request to 
```bash
  /cart/<cartId>
```
**Note** : replace **\<cartId\>** with you cartId.

**3.** Get all the items in the cart by making **GET** request to
```bash
  /cart/<cartId>/items
```
**Note** : replace **\<cartId\>** with you cartId.

**4.** To add items to the cart, make **PUT** request by passing **name , category , price** as request body.
The endpoint is given below:
```bash
  /cart/<cartId>/add
```
**Note** : replace **\<cartId\>** with you cartId.
From the response JSON, copy **itemId** for next step.

**5.** To remove the item from the cart, make **DELETE** request to,
```bash
  /cart/<cartId>/remove/<itemId>
```
**Note** : replace **\<cartId\>** with your cartId and **\<itemId\>** with copied itemId.
