# Importing necessary libraries
from flask import Flask, request
from flask_cors import CORS  # Import flask_cors
from util import calculate_delivery_fee

# Initializing flask application
app = Flask(__name__)
CORS(app)  # Use flask_cors to allow requests


# Defining POST endpoint, where it will receive the JSON payload and calculate the delivery fee
@app.route('/calculate_fee', methods=['POST'])
def calculate_fee_endpoint():
    data = request.get_json()

    # Implementing some basic Error Handling
    # Checking that all necessary fields are present
    required_fields = ['cart_value', 'delivery_distance', 'number_of_items', 'time']
    for field in required_fields:
        if field not in data:
            return {'error': f'Missing required field: {field}'}, 400

    # Checking that all fields are of the correct type
    if not isinstance(data['cart_value'], int):
        return {'error': 'cart_value must be an integer'}, 400
    if not isinstance(data['delivery_distance'], int):
        return {'error': 'delivery_distance must be an integer'}, 400
    if not isinstance(data['number_of_items'], int):
        return {'error': 'number_of_items must be an integer'}, 400
    if not isinstance(data['time'], str):
        return {'error': 'time must be a string'}, 400

    # Calculating the delivery fee
    try:
        delivery_fee = calculate_delivery_fee(data)
    except Exception as e:
        return {'error': str(e)}, 500

    return {'delivery_fee': delivery_fee}


if __name__ == '__main__':
    app.run(debug=True)
