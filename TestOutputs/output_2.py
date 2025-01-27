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
	order_date = db.Column(db.String)
	status = db.Column(db.String)

class Customer(db.Model):
	id = db.Column(db.String, primary_key=True)
	full_name = db.Column(db.String)
	email = db.Column(db.String)
	phone_number = db.Column(db.String)



# Create the database
with app.app_context():
	db.create_all()


	try:
		order = Order(
			id = 'O1001',
			customer_name = 'John Doe',
			price = '250.0',
			order_date = '2025-01-25',
			status = 'Pending'
		)
		db.session.add(order)
		db.session.commit()
	except:
		pass


	try:
		customer = Customer(
			id = 'C1001',
			full_name = 'John Doe',
			email = 'john.doe@example.com',
			phone_number = '123-456-7890'
		)
		db.session.add(customer)
		db.session.commit()
	except:
		pass


	try:
		order = Order.query.get('O1001')
		if order:
			order.status = 'Shipped'
			order.order_date = 'kir'
			db.session.commit()
	except:
		pass


	try:
		customer = Customer.query.get('C1001')
		if customer:
			db.session.delete(customer)
			db.session.commit()
	except:
		pass


	try:
		entries = order.query.all()
		for entry in entries:
			print(entry)
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
		order_date=data['order_date'],
		status=data['status'],
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
		order.order_date = data.get('order_date', order.order_date)
		order.status = data.get('status', order.status)
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
		"order_date": order.order_date,
		"status": order.status
	} for order in orders]
	return jsonify(order_list), 200


# Create Customer
@app.route('/createCustomer', methods=['POST'])
def create_customer():
	data = request.get_json()
	customer = Customer(
		id=data['id'],
		full_name=data['full_name'],
		email=data['email'],
		phone_number=data['phone_number'],
		)
	db.session.add(customer)
	db.session.commit()
	return jsonify({"message": "Customer created successfully"}), 201


# Delete Customer
@app.route('/deleteCustomer', methods=['POST'])
def delete_customer():
	data = request.get_json()
	customer = Customer.query.get(data['id'])
	if customer:
		db.session.delete(customer)
		db.session.commit()
		return jsonify({"message": "Customer deleted successfully"}), 200
	else:
		return jsonify({"error": "Customer not found"}), 404


# Update Customer
@app.route('/updateCustomer', methods=['POST'])
def update_customer():
	data = request.get_json()
	customer = Customer.query.get(data['id'])
	if customer:
		customer.full_name = data.get('full_name', customer.full_name)
		customer.email = data.get('email', customer.email)
		customer.phone_number = data.get('phone_number', customer.phone_number)
		db.session.commit()
		return jsonify({"message": "Customer updated successfully"}), 200
	else:
		return jsonify({"error": "Customer not found"}), 404


# List Customers
@app.route('/listCustomers', methods=['GET'])
def list_customers():
	customers = Customer.query.all()
	customer_list = [{
		"id": customer.id,
		"full_name": customer.full_name,
		"email": customer.email,
		"phone_number": customer.phone_number
	} for customer in customers]
	return jsonify(customer_list), 200


if __name__ == '__main__':
	app.run(debug=True)