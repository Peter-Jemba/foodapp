from flask import Blueprint, request, jsonify, url_for, redirect
from models.model import Menu, User, menus_db, user_db


menu_blueprint = Blueprint('Menu_blueprint', __name__)

@menu_blueprint.route('/menus', methods=["POST", "GET"])
def menus():
    if request.method == "POST":
 
        new_menu = Menu(request.json["name"], request.json["price"])
        menus_db.append(new_menu)
        menus_list = [{"name": item.name, "price": item.price} for item in menus_db]
        data = jsonify({"message": "successfully created!", "menu": menus_list}), 201
    else:
        menus_list = [{"name": item.name, "price": item.price} for item in menus_db]
        data = jsonify({"menu": menus_list}), 200
    return data

@menu_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        if request.json["username"] in user_db:
            return jsonify({"message":"exits"})
        else:
            new_user = User(request.json["username"], request.json["password"])
            user_db.append(new_user)
        return jsonify({"message":"User has been registered"})

@menu_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if request.json in user_db:
            return jsonify({"message":"User logged in"})
        else:
            return jsonify({"message":"User provided wrong credentials"})

