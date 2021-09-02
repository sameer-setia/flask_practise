from models import db, Employee
from flask_restful import Resource
from flask import request


class EmployeeList(Resource):
    def get(self):
        employees = Employee.query.all()
        return {'data': [x.json() for x in employees]}
 
    def post(self):
        data = request.get_json()
        emp = Employee(data['name'],data['salary'],data['designation'])
        db.session.add(emp)
        db.session.commit()
        return {'msg': 'employee added successfully'}

class EmployeeView(Resource):
    def get(self,name):
        employee = Employee.query.filter_by(name=name).first()
        if employee:
            return employee.json()
        return {'message':'employee not found'},404
 
    def put(self,name):
        data = request.get_json()
 
        employee = Employee.query.filter_by(name=name).first()
 
        if employee:
            employee.salary = data["salary"]
            employee.designation = data["designation"]
        else:
            employee = Employee(name=name,**data)
 
        db.session.add(employee)
        db.session.commit()
 
        return employee.json()
 
    def delete(self,name):
        employee = Employee.query.filter_by(name=name).first()
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return {'message':'Deleted'}
        else:
            return {'message': 'employee not found'},404
