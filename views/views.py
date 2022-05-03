from flask import Blueprint, request, jsonify, url_for, redirect
from models.model import Order, orders_db


order_blueprint = Blueprint('Order_blueprint', __name__)

@order_blueprint.route('/orders', methods=["POST", "GET"])
def orders():
    if request.method == "POST":
        new_order = Order(request.json["name"], request.json["price"])
        orders_db.append(new_order)
        orders_list = [{"name": item.name, "price": item.price} for item in orders_db]
        data = jsonify({"message": "successfully created!", "data": orders_list}), 201
    else:
        orders_list = [{"name": item.name, "price": item.price} for item in orders_db]
        data = jsonify({"data": orders_list}), 200
    return data

@order_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.json['username'], request.json["password"]
        return user
    return jsonify({"message": "User not found"})

@order_blueprint.route('/orders/<string:name>', methods=['GET'])
def get_order(name):
    if request.method == "GET":
        orders_list = Order(request.json[name])
        return jsonify(orders_list)
    return jsonify({'message': 'Order not found'}), 200