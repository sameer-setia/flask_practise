import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy()
api = Api(app)
migrate = Migrate(app, db)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'loremipsum'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
from models import Employee

@login_manager.user_loader
def load_user(id):
        return Employee.query.get(int(id))

@app.before_first_request
def create_table():
    db.create_all()
from employee import employee
app.register_blueprint(employee)
from auth import auth
app.register_blueprint(auth)
from main import main
app.register_blueprint(main)


app.debug = True
if __name__ == '__main__':
    app.run()