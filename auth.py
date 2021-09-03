from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import Employee
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import login_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    employee = Employee.query.filter_by(email=email).first()
    if employee:
        flash('Email already exists.')
        return redirect(url_for('auth.signup'))
    new_emp = Employee(
        name=name,
        email=email,
        password=generate_password_hash(password, method='sha256'),
        salary = 0,
        designation= 'intern'
    )
    db.session.add(new_emp)
    db.session.commit()
    return redirect(url_for('auth.login'))

...
@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Employee.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))