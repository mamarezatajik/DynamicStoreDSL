# Import required libraries for API interactions
import json
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Import CORS
from random import randint

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
db = SQLAlchemy(app)

# This header file ensures all the dependencies are included before the actual DSL function implementation


class Order(db.Model):
	id = db.Column(db.String, primary_key=True)
	customer_name = db.Column(db.String)
	total_amount = db.Column(db.Float)
	status = db.Column(db.String)
	delivery_date = db.Column(db.String)



# Create the database
with app.app_context():
	db.create_all()


	try:
		order = Order(
			id = 'O8002',
			customer_name = 'Emily Brown',
			total_amount = '299.99',
			status = 'Pending',
			delivery_date = '2025-02-05'
		)
		db.session.add(order)
		db.session.commit()
	except:
		pass


	try:
		order = Order.query.get('O8002')
		if order:
			order.status = 'Completed'
			db.session.commit()
	except:
		pass


# Create Order
@app.route('/createOrder', methods=['POST'])
def create_order():
	data = request.get_json()
	order = Order(
		id=data['id'],
		customer_name=data['customer_name'],
		total_amount=data['total_amount'],
		status=data['status'],
		delivery_date=data['delivery_date'],
		)
	db.session.add(order)
	db.session.commit()
	return jsonify({"message": "Order created successfully"}), 201


# Delete Order
@app.route('/deleteOrder', methods=['POST'])
def delete_order():
	data = request.get_json()
	order = Order.query.get(data['id'])
	if order:
		db.session.delete(order)
		db.session.commit()
		return jsonify({"message": "Order deleted successfully"}), 200
	else:
		return jsonify({"error": "Order not found"}), 404


# Update Order
@app.route('/updateOrder', methods=['POST'])
def update_order():
	data = request.get_json()
	order = Order.query.get(data['id'])
	if order:
		order.customer_name = data.get('customer_name', order.customer_name)
		order.total_amount = data.get('total_amount', order.total_amount)
		order.status = data.get('status', order.status)
		order.delivery_date = data.get('delivery_date', order.delivery_date)
		db.session.commit()
		return jsonify({"message": "Order updated successfully"}), 200
	else:
		return jsonify({"error": "Order not found"}), 404


# List Orders
@app.route('/listOrders', methods=['GET'])
def list_orders():
	orders = Order.query.all()
	order_list = [{
		"id": order.id,
		"customer_name": order.customer_name,
		"total_amount": order.total_amount,
		"status": order.status,
		"delivery_date": order.delivery_date
	} for order in orders]
	return jsonify(order_list), 200


if __name__ == '__main__':
	app.run(debug=True)