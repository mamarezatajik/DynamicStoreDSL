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
	price = db.Column(db.Float)
	stock_quantity = db.Column(db.Integer)
	category = db.Column(db.String)



# Create the database
with app.app_context():
	db.create_all()


	try:
		product = Product(
			id = 'P1001',
			name = 'Smartphone',
			price = '899.99',
			stock_quantity = '150',
			category = 'Electronics'
		)
		db.session.add(product)
		db.session.commit()
	except:
		pass


# Create Product
@app.route('/createProduct', methods=['POST'])
def create_product():
	data = request.get_json()
	product = Product(
		id=data['id'],
		name=data['name'],
		price=data['price'],
		stock_quantity=data['stock_quantity'],
		category=data['category'],
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
		product.price = data.get('price', product.price)
		product.stock_quantity = data.get('stock_quantity', product.stock_quantity)
		product.category = data.get('category', product.category)
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
		"price": product.price,
		"stock_quantity": product.stock_quantity,
		"category": product.category
	} for product in products]
	return jsonify(product_list), 200


if __name__ == '__main__':
	app.run(debug=True)