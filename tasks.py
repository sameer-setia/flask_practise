import os
from celery import Celery
from models import db, Employee
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Celery('tasks', broker=os.environ.get('CELERY_BROKER'))

@app.task(name='add')
def add(x, y):
    return x + y

@app.task(name='send_sms')
def send_sms():

    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    print(account_sid, auth_token)
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Hello! Your otp for login is 1234.",
                     from_='+13347218537',
                     to='+918847583453'
                 )


@app.task(name='send_mail')
def send_mail():
    message = Mail(
    from_email='sameersetia17@gmail.com',
    to_emails='sameersetia37@gmail.com',
    subject='Test Email',
    html_content='Hello This is a test mail.')

    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    sg.send(message)
    return 'mail sent'



@app.task(name='add_employee')
def add_employee(name, salary, designation):
    emp = Employee(name, salary, designation)
    db.session.add(emp)
    db.session.commit()
    return emp.name