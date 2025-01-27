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


class Inventory(db.Model):
	id = db.Column(db.String, primary_key=True)
	item_name = db.Column(db.String)
	quantity = db.Column(db.Integer)
	price_per_unit = db.Column(db.Float)
	supplier = db.Column(db.String)



# Create the database
with app.app_context():
	db.create_all()


	try:
		inventory = Inventory(
			id = 'I5001',
			item_name = 'Laptop',
			quantity = '50',
			price_per_unit = '1200.00',
			supplier = 'Tech Supplies Inc.'
		)
		db.session.add(inventory)
		db.session.commit()
	except:
		pass


	try:
		inventory = Inventory.query.get('I5001')
		if inventory:
			inventory.quantity = '45'
			db.session.commit()
	except:
		pass


	try:
		entries = inventory.query.all()
		for entry in entries:
			print(entry)
	except:
		pass


# Create Inventory
@app.route('/createInventory', methods=['POST'])
def create_inventory():
	data = request.get_json()
	inventory = Inventory(
		id=data['id'],
		item_name=data['item_name'],
		quantity=data['quantity'],
		price_per_unit=data['price_per_unit'],
		supplier=data['supplier'],
		)
	db.session.add(inventory)
	db.session.commit()
	return jsonify({"message": "Inventory created successfully"}), 201


# Delete Inventory
@app.route('/deleteInventory', methods=['POST'])
def delete_inventory():
	data = request.get_json()
	inventory = Inventory.query.get(data['id'])
	if inventory:
		db.session.delete(inventory)
		db.session.commit()
		return jsonify({"message": "Inventory deleted successfully"}), 200
	else:
		return jsonify({"error": "Inventory not found"}), 404


# Update Inventory
@app.route('/updateInventory', methods=['POST'])
def update_inventory():
	data = request.get_json()
	inventory = Inventory.query.get(data['id'])
	if inventory:
		inventory.item_name = data.get('item_name', inventory.item_name)
		inventory.quantity = data.get('quantity', inventory.quantity)
		inventory.price_per_unit = data.get('price_per_unit', inventory.price_per_unit)
		inventory.supplier = data.get('supplier', inventory.supplier)
		db.session.commit()
		return jsonify({"message": "Inventory updated successfully"}), 200
	else:
		return jsonify({"error": "Inventory not found"}), 404


# List Inventorys
@app.route('/listInventorys', methods=['GET'])
def list_inventorys():
	inventorys = Inventory.query.all()
	inventory_list = [{
		"id": inventory.id,
		"item_name": inventory.item_name,
		"quantity": inventory.quantity,
		"price_per_unit": inventory.price_per_unit,
		"supplier": inventory.supplier
	} for inventory in inventorys]
	return jsonify(inventory_list), 200


if __name__ == '__main__':
	app.run(debug=True)