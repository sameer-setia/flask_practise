import os
from celery import Celery
from models import db, Employee

app = Celery('celery_config', broker=os.environ.get('CELERY_BROKER'))

@app.task
def add(x, y):
    return x + y

@app.task(name='add_employee')
def add_employee(name, salary, designation):
    emp = Employee(name, salary, designation)
    db.session.add(emp)
    db.session.commit()
    return emp.name