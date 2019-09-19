from flask import Flask, request
from loguru import logger
import json


class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)

    def __str__(self):
        return f'{self.name} - {self.price}'


class FoodOrder:
    def __init__(self, id):
        self.id = id
        self.item_list = []
        self.item_total = 0
        self.delivery_charge = 20
        self.total_price = 0 + self.delivery_charge

    def add_item(self, food_item):
        self.item_list.append(food_item)
        self.item_total += food_item.price
        self.total_price += food_item.price

    def get_pricing_details(self):
        order_details = {}
        order_details['item_total'] = self.item_total
        order_details['delivery_charge'] = self.delivery_charge
        order_details['total_price'] = self.total_price
        return order_details

    def get_item_details(self):
        all_item_details = []
        for item in self.item_list:
            item_details = {'name': item.name,
                            'price': item.price}
            all_item_details.append(item_details)

        return all_item_details



    def __str__(self):
        return f'{self.id} : {self.total_price}'

food_menu = {}
order_list = []

app = Flask(__name__)

@app.route('/')
def home():
    x = int('abcd')
    return "hello world"

@app.route('/add_item', methods=['POST'])
def add_item():
    food_name = request.form.get('name')
    food_price = request.form.get('price')
    food_item = FoodItem(food_name, food_price)
    logger.debug(food_item)
    food_menu[food_item.name] = food_item
    logger.debug(food_menu)

    return "got the food item."

@app.route('/show_menu')
def show_menu():
    menu_list = []
    for food_item in food_menu.values():
        menu_list.append((food_item.name, food_item.price))
    logger.debug(menu_list)

    return json.dumps(menu_list)

@app.route('/take_order', methods=['POST'])
def take_order():
    food_name = request.form.get('name')
    food_quantity = request.form.get('quantity')
    food_order = FoodOrder(len(order_list))
    food_item = food_menu[food_name]
    for i in range(int(food_quantity)):
        food_order.add_item(food_item)

    order_list.append(food_order)

    logger.debug(order_list)

    return "Order saved"

@app.route('/show_orders')
def show_orders():
    all_order_details = []
    for order in order_list:
        single_order_details = {}
        single_order_details['pricing_details'] = order.get_pricing_details() 
        single_order_details['item_details'] = order.get_item_details()
        all_order_details.append(single_order_details)

    logger.debug(all_order_details)
    return json.dumps(all_order_details)

if __name__ == '__main__':
    app.run(debug=True)