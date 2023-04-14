from ebay_rest import API, Error
import logging 
import json 

with open('ebay_rest.json') as f:
    cred = json.load(f)

application = cred["applications"]["production_1"]
user = cred["users"]["production_1"]
header = cred['headers']['US']


logging.basicConfig(filename="app.log", level= logging.INFO)


try:
    api = API(application=application, user=user, header=header)
except Error as error:
    print(f'Error {error.number} is {error.reason}  {error.detail}.\n')
else:
    try:
        orders = api.sell_fulfillment_get_orders(limit = 1)
        for order in orders:
            print(order)
    except Error as error:
        print(f'Error {error.number} is {error.reason} {error.detail}.\n')
    else:
        pass
