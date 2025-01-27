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


class Supplier(db.Model):
	id = db.Column(db.String, primary_key=True)
	company_name = db.Column(db.String)
	contact_email = db.Column(db.String)
	phone_number = db.Column(db.String)



# Create the database
with app.app_context():
	db.create_all()


	try:
		supplier = Supplier(
			id = 'S4004',
			company_name = 'Fresh Supplies Inc.',
			contact_email = 'contact@freshsupplies.com',
			phone_number = '123-987-6543'
		)
		db.session.add(supplier)
		db.session.commit()
	except:
		pass


# Create Supplier
@app.route('/createSupplier', methods=['POST'])
def create_supplier():
	data = request.get_json()
	supplier = Supplier(
		id=data['id'],
		company_name=data['company_name'],
		contact_email=data['contact_email'],
		phone_number=data['phone_number'],
		)
	db.session.add(supplier)
	db.session.commit()
	return jsonify({"message": "Supplier created successfully"}), 201


# Delete Supplier
@app.route('/deleteSupplier', methods=['POST'])
def delete_supplier():
	data = request.get_json()
	supplier = Supplier.query.get(data['id'])
	if supplier:
		db.session.delete(supplier)
		db.session.commit()
		return jsonify({"message": "Supplier deleted successfully"}), 200
	else:
		return jsonify({"error": "Supplier not found"}), 404


# Update Supplier
@app.route('/updateSupplier', methods=['POST'])
def update_supplier():
	data = request.get_json()
	supplier = Supplier.query.get(data['id'])
	if supplier:
		supplier.company_name = data.get('company_name', supplier.company_name)
		supplier.contact_email = data.get('contact_email', supplier.contact_email)
		supplier.phone_number = data.get('phone_number', supplier.phone_number)
		db.session.commit()
		return jsonify({"message": "Supplier updated successfully"}), 200
	else:
		return jsonify({"error": "Supplier not found"}), 404


# List Suppliers
@app.route('/listSuppliers', methods=['GET'])
def list_suppliers():
	suppliers = Supplier.query.all()
	supplier_list = [{
		"id": supplier.id,
		"company_name": supplier.company_name,
		"contact_email": supplier.contact_email,
		"phone_number": supplier.phone_number
	} for supplier in suppliers]
	return jsonify(supplier_list), 200


if __name__ == '__main__':
	app.run(debug=True)