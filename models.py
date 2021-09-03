from app import db
from flask_login import UserMixin

class Employee(UserMixin, db.Model):
    __tablename__ = 'employee'
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    salary = db.Column(db.Integer())
    designation = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(100))
 
    def __init__(self, name, salary, designation, email, password):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.email = email
        self.password = password
    
    def json(self):
        return {"name":self.name, "salary":self.salary, "designation":self.designation,"email":self.email}