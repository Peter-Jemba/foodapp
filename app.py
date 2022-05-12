from flask import Flask, jsonify, request
from views.views import menu_blueprint

app = Flask(__name__)
app.register_blueprint(menu_blueprint)

menus = [
    {
        'name': 'Pilata',
        'foods': [
            {
                'name': 'Chicken Pilao',
                'price': '5.99'
            }
        ]
    }
]

#POST /menu data: {name}
@app.route('/menu', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    new_menu = {
        'name': request_data['name'],
        'foods': []
    }
    menus.append(new_menu)
    return jsonify(new_menu), 201

#GET /menu/<string:name>
@app.route('/menu/<string:name>')
def get_order(name):
    for menu in menus:
        if menu['name'] == name:
            return jsonify(menu)
    return jsonify({'message': 'Order not found'}), 200

#GET /menu
@app.route('/menu')
def get_menus():
    return jsonify({'menus': menus}), 200

#POST /menu/<string:name>/food {name:, price:}
@app.route('/menu/<string:name>/food', methods=['POST'])
def create_food_in_menu(name):
    request_data = request.get_json()
    for menu in menus:
        if menu['name'] == name:
            new_menu ={
                'name': request_data['name'],
                'price': request_data['price']
            }
            menu['foods'].append(new_menu)
            return jsonify(new_menu)

#GET /menu/<string:name>/food
@app.route('/menu/<string:name>/food')
def get_food_in_menu(name):
    for menu in menus:
        if menu['name'] == name:
            return jsonify({'foods': menu['foods']})
    return jsonify({'message': 'Order not found'})

@app.route('/')
def home():
    return "Hello, world!"

if __name__ =='__app__':
    app.run(port=5000, debug=True)