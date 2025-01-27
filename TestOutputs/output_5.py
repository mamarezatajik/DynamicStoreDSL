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


class Employee(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)
	role = db.Column(db.String)
	salary = db.Column(db.Float)
	department = db.Column(db.String)



# Create the database
with app.app_context():
	db.create_all()


	try:
		employee = Employee(
			id = 'E1001',
			name = 'Sara Lee',
			role = 'Manager',
			salary = '65000.0',
			department = 'Sales'
		)
		db.session.add(employee)
		db.session.commit()
	except:
		pass


	try:
		employee = Employee.query.get('E1001')
		if employee:
			db.session.delete(employee)
			db.session.commit()
	except:
		pass


	try:
		entries = employee.query.all()
		for entry in entries:
			print(entry)
	except:
		pass


# Create Employee
@app.route('/createEmployee', methods=['POST'])
def create_employee():
	data = request.get_json()
	employee = Employee(
		id=data['id'],
		name=data['name'],
		role=data['role'],
		salary=data['salary'],
		department=data['department'],
		)
	db.session.add(employee)
	db.session.commit()
	return jsonify({"message": "Employee created successfully"}), 201


# Delete Employee
@app.route('/deleteEmployee', methods=['POST'])
def delete_employee():
	data = request.get_json()
	employee = Employee.query.get(data['id'])
	if employee:
		db.session.delete(employee)
		db.session.commit()
		return jsonify({"message": "Employee deleted successfully"}), 200
	else:
		return jsonify({"error": "Employee not found"}), 404


# Update Employee
@app.route('/updateEmployee', methods=['POST'])
def update_employee():
	data = request.get_json()
	employee = Employee.query.get(data['id'])
	if employee:
		employee.name = data.get('name', employee.name)
		employee.role = data.get('role', employee.role)
		employee.salary = data.get('salary', employee.salary)
		employee.department = data.get('department', employee.department)
		db.session.commit()
		return jsonify({"message": "Employee updated successfully"}), 200
	else:
		return jsonify({"error": "Employee not found"}), 404


# List Employees
@app.route('/listEmployees', methods=['GET'])
def list_employees():
	employees = Employee.query.all()
	employee_list = [{
		"id": employee.id,
		"name": employee.name,
		"role": employee.role,
		"salary": employee.salary,
		"department": employee.department
	} for employee in employees]
	return jsonify(employee_list), 200


if __name__ == '__main__':
	app.run(debug=True)