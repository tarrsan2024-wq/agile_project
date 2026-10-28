 from flask import Flask, request, jsonify

app = Flask(__name__)
payments = [{"student_id": "24MIS0060", "amount": 25000}]
dues = {"24MIS0001": 5000, "24MIS0020": 1200}

@app.route('/')
def home():
    return "Fee System v3: Full System Active"

@app.route('/add_payment', methods=['POST'])
def add_payment():
    data = request.json
    payments.append(data)
    return jsonify({"message": "Payment recorded successfully", "data": data}), 201

@app.route('/view_dues', methods=['GET'])
def view_dues():
    return jsonify({"pending_fees": dues}), 200

@app.route('/report', methods=['GET'])
def fee_report():
    total_collected = sum(p.get('amount', 0) for p in payments)
    return jsonify({
        "total_payments_recorded": len(payments),
        "total_amount_collected": total_collected,
        "status": "Summary Generated"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
