from app import db
from models import Employee
from flask import request, Blueprint

employee = Blueprint('employee', __name__)

@employee.route('/employees')
def employee_listing():
    employees = Employee.query.all()
    return {'data': [x.json() for x in employees]}
    
@employee.route('/add-employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    emp = Employee(data['name'],data['salary'],data['designation'],data['email'],data['password'])
    db.session.add(emp)
    db.session.commit()
    return {'msg': f'{emp.name} added successfully'}
    

@employee.route('/employees/<string:name>')
def get_employee(name):
        employee = Employee.query.filter_by(name=name).first()
        if employee:
            return employee.json()
        return {'message':'employee not found'},404

@employee.route('/edit/<string:name>', methods=['POST'])
def put(name):
    data = request.get_json()
    employee = Employee.query.filter_by(name=name).first()
 
    if employee:
        employee.salary = data["salary"]
        employee.designation = data["designation"]
        employee.email = data['email']
    else:
        employee = Employee(name=name,**data)
 
    db.session.add(employee)
    db.session.commit()
 
    return employee.json()

@employee.route('/delete/<string:name>', methods=['POST'])
def delete(name):
    employee = Employee.query.filter_by(name=name).first()
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return {'message':f'Deleted {name}'}
    else:
        return {'message': 'employee not found'},404
