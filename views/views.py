from flask import Blueprint, request, jsonify, url_for, redirect
from models.model import Order, User, orders_db, user_db


order_blueprint = Blueprint('Order_blueprint', __name__)

@order_blueprint.route('/orders', methods=["POST", "GET"])
def orders():
    if request.method == "POST":
 
        new_order = Order(request.json["name"], request.json["price"])
        orders_db.append(new_order)
        orders_list = [{"name": item.name, "price": item.price} for item in orders_db]
        data = jsonify({"message": "successfully created!", "menu": orders_list}), 201
    else:
        orders_list = [{"name": item.name, "price": item.price} for item in orders_db]
        data = jsonify({"menu": orders_list}), 200
    return data

@order_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        if request.json["username"] in user_db:
            return jsonify({"message":"exits"})
        else:
            new_user = User(request.json["username"], request.json["password"])
            user_db.append(new_user)
        return jsonify({"message":"User has been registered"})

@order_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if request.json in user_db:
            return jsonify({"message":"User logged in"})
        else:
            return jsonify({"message":"User provided wrong credentials"})

