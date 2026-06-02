from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "Calculator API is running!"


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    operation = data.get('operation')

    if operation == 'add':
        result = add(a, b)
    elif operation == 'subtract':
        result = subtract(a, b)
    elif operation == 'multiply':
        result = multiply(a, b)
    elif operation == 'divide':
        try:
            result = divide(a, b)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
