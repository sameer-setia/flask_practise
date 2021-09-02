from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employee'
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    salary = db.Column(db.Integer())
    designation = db.Column(db.String(80))
 
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
    
    def json(self):
        return {"name":self.name, "salary":self.salary, "designation":self.designation}