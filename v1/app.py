 from flask import Flask, request, jsonify

app = Flask(__name__)
payments = []

@app.route('/')
def home():
    return "Fee System v1: Add Payment Active"

@app.route('/add_payment', methods=['POST'])
def add_payment():
    data = request.json
    if not data or 'amount' not in data:
        return jsonify({"error": "Invalid payment data"}), 400
    payments.append(data)
    return jsonify({"message": "Payment recorded successfully", "data": data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

