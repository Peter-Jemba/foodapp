from flask import Flask, jsonify, request
from views.views import order_blueprint

app = Flask(__name__)
app.register_blueprint(order_blueprint)

orders = [
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

#POST /order data: {name}
@app.route('/order', methods=['POST'])
def create_order():
    request_data = request.get_json()
    new_order = {
        'name': request_data['name'],
        'foods': []
    }
    orders.append(new_order)
    return jsonify(new_order), 201

#GET /order/<string:name>
@app.route('/order/<string:name>')
def get_order(name):
    for order in orders:
        if order['name'] == name:
            return jsonify(order)
    return jsonify({'message': 'Order not found'}), 200

#GET /store
@app.route('/order')
def get_orders():
    return jsonify({'orders': orders}), 200

#POST /order/<string:name>/food {name:, price:}
@app.route('/order/<string:name>/food', methods=['POST'])
def create_food_in_order(name):
    request_data = request.get_json()
    for order in orders:
        if order['name'] == name:
            new_food ={
                'name': request_data['name'],
                'price': request_data['price']
            }
            order['foods'].append(new_food)
            return jsonify(new_food)

#GET /order/<string:name>/food
@app.route('/order/<string:name>/food')
def get_food_in_order(name):
    for order in orders:
        if order['name'] == name:
            return jsonify({'foods': order['foods']})
    return jsonify({'message': 'Order not found'})

@app.route('/')
def home():
    return "Hello, world!"

if __name__ =='__app__':
    app.run(debug=True)