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


class Product(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)
	category = db.Column(db.String)
	price = db.Column(db.Float)
	stock_quantity = db.Column(db.Integer)
	supplier = db.Column(db.String)

class Order(db.Model):
	id = db.Column(db.String, primary_key=True)
	customer_name = db.Column(db.String)
	total_amount = db.Column(db.Float)
	order_date = db.Column(db.String)
	status = db.Column(db.String)
	payment_method = db.Column(db.String)

class Customer(db.Model):
	id = db.Column(db.String, primary_key=True)
	full_name = db.Column(db.String)
	email = db.Column(db.String)
	phone_number = db.Column(db.String)
	loyalty_points = db.Column(db.Integer)
	membership = db.Column(db.String)



# Create the database
with app.app_context():
	db.create_all()


	try:
		product = Product(
			id = 'P4001',
			name = 'Wireless Mouse',
			category = 'Electronics',
			price = '25.99',
			stock_quantity = '100',
			supplier = 'TechWorld Inc.'
		)
		db.session.add(product)
		db.session.commit()
	except:
		pass


	try:
		customer = Customer(
			id = 'C4001',
			full_name = 'Michael Brown',
			email = 'michael.brown@example.com',
			phone_number = '321-654-0987',
			loyalty_points = '150',
			membership = 'Gold'
		)
		db.session.add(customer)
		db.session.commit()
	except:
		pass


	try:
		order = Order(
			id = 'O4001',
			customer_name = 'Michael Brown',
			total_amount = '51.98',
			order_date = '2025-02-02',
			status = 'Pending',
			payment_method = 'Credit Card'
		)
		db.session.add(order)
		db.session.commit()
	except:
		pass


	try:
		product = Product.query.get('P4001')
		if product:
			product.stock_quantity = '98'
			db.session.commit()
	except:
		pass


	try:
		customer = Customer.query.get('C4001')
		if customer:
			customer.loyalty_points = '175'
			db.session.commit()
	except:
		pass


	try:
		product = Product.query.get('P4001')
		if product:
			db.session.delete(product)
			db.session.commit()
	except:
		pass


	try:
		product = Product(
			id = 'P4002',
			name = 'Gaming Keyboard',
			category = 'Electronics',
			price = '49.99',
			stock_quantity = '50',
			supplier = 'GamingHub LLC'
		)
		db.session.add(product)
		db.session.commit()
	except:
		pass


	try:
		order = Order.query.get('O4001')
		if order:
			order.status = 'Completed'
			order.total_amount = '46.78'
			db.session.commit()
	except:
		pass


	try:
		entries = product.query.all()
		for entry in entries:
			print(entry)
	except:
		pass


	try:
		entries = customer.query.all()
		for entry in entries:
			print(entry)
	except:
		pass


	try:
		entries = order.query.all()
		for entry in entries:
			print(entry)
	except:
		pass


# Create Product
@app.route('/createProduct', methods=['POST'])
def create_product():
	data = request.get_json()
	product = Product(
		id=data['id'],
		name=data['name'],
		category=data['category'],
		price=data['price'],
		stock_quantity=data['stock_quantity'],
		supplier=data['supplier'],
		)
	db.session.add(product)
	db.session.commit()
	return jsonify({"message": "Product created successfully"}), 201


# Delete Product
@app.route('/deleteProduct', methods=['POST'])
def delete_product():
	data = request.get_json()
	product = Product.query.get(data['id'])
	if product:
		db.session.delete(product)
		db.session.commit()
		return jsonify({"message": "Product deleted successfully"}), 200
	else:
		return jsonify({"error": "Product not found"}), 404


# Update Product
@app.route('/updateProduct', methods=['POST'])
def update_product():
	data = request.get_json()
	product = Product.query.get(data['id'])
	if product:
		product.name = data.get('name', product.name)
		product.category = data.get('category', product.category)
		product.price = data.get('price', product.price)
		product.stock_quantity = data.get('stock_quantity', product.stock_quantity)
		product.supplier = data.get('supplier', product.supplier)
		db.session.commit()
		return jsonify({"message": "Product updated successfully"}), 200
	else:
		return jsonify({"error": "Product not found"}), 404


# List Products
@app.route('/listProducts', methods=['GET'])
def list_products():
	products = Product.query.all()
	product_list = [{
		"id": product.id,
		"name": product.name,
		"category": product.category,
		"price": product.price,
		"stock_quantity": product.stock_quantity,
		"supplier": product.supplier
	} for product in products]
	return jsonify(product_list), 200


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
		payment_method=data['payment_method'],
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
		order.payment_method = data.get('payment_method', order.payment_method)
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
		"status": order.status,
		"payment_method": order.payment_method
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
		loyalty_points=data['loyalty_points'],
		membership=data['membership'],
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
		customer.loyalty_points = data.get('loyalty_points', customer.loyalty_points)
		customer.membership = data.get('membership', customer.membership)
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
		"phone_number": customer.phone_number,
		"loyalty_points": customer.loyalty_points,
		"membership": customer.membership
	} for customer in customers]
	return jsonify(customer_list), 200


if __name__ == '__main__':
	app.run(debug=True)