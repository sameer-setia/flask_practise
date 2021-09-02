import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from employee import EmployeeList, EmployeeView

app = Flask(__name__)
db = SQLAlchemy()
api = Api(app)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(EmployeeList, '/employees')
api.add_resource(EmployeeView,'/employees/<string:name>')

app.debug = True
if __name__ == '__main__':
    app.run()