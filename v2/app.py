 from flask import Flask, request, jsonify

app = Flask(__name__)
payments = []
dues = {"24MIS0001": 5000, "24MIS0020": 1200, "24MIS0060": 15000}

@app.route('/')
def home():
    return "Fee System v2: Add Payment & View Dues Active"

@app.route('/add_payment', methods=['POST'])
def add_payment():
    data = request.json
    payments.append(data)
    return jsonify({"message": "Payment recorded successfully", "data": data}), 201

@app.route('/view_dues', methods=['GET'])
def view_dues():
    return jsonify({"pending_fees": dues}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
