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


class Customer(db.Model):
	id = db.Column(db.String, primary_key=True)
	full_name = db.Column(db.String)
	email = db.Column(db.String)
	phone_number = db.Column(db.String)
	address = db.Column(db.String)



# Create the database
with app.app_context():
	db.create_all()


	try:
		customer = Customer(
			id = 'C7003',
			full_name = 'Bob Johnson',
			email = 'bob.johnson@example.com',
			phone_number = '987-654-3210',
			address = '123 Maple Street, Springfield'
		)
		db.session.add(customer)
		db.session.commit()
	except:
		pass


# Create Customer
@app.route('/createCustomer', methods=['POST'])
def create_customer():
	data = request.get_json()
	customer = Customer(
		id=data['id'],
		full_name=data['full_name'],
		email=data['email'],
		phone_number=data['phone_number'],
		address=data['address'],
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
		customer.address = data.get('address', customer.address)
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
		"address": customer.address
	} for customer in customers]
	return jsonify(customer_list), 200


if __name__ == '__main__':
	app.run(debug=True)