from datetime import datetime
from invoice import db, login_manager
from flask import current_app
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    mobile = db.Column(db.String())
    location = db.Column(db.String())
    facebook = db.Column(db.String())
    instagram = db.Column(db.String())
    linkedin = db.Column(db.String())
    twitter = db.Column(db.String())
    clients = db.relationship('Client', backref='customer', lazy=True)
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)
    
    
    def generate_reset_token(self):
        s = Serializer(current_app.config['SECRET_KEY'], salt='reset')
        return s.dumps({'reset': self.id})
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'], salt='reset')
        try:
            data = s.loads(token, max_age=3600)
        except:
            return None
        user = User.query.get(data.get('reset'))
        if user is None:
            return None
        return user 
    
    def __repr__(self):
        return f'{self.username} - {self.email}'
    

class Client(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    client_type = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    phone = db.Column(db.String(), unique=True, nullable=False)
    website = db.Column(db.String())
    address = db.Column(db.Text())
    logo = db.Column(db.String(), default='logo.jpg')
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    invoices = db.relationship('Invoice', backref='client', lazy=True)
    date_joined = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'{self.name} - {self.email}'
    
    
class InvoiceItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    details = db.Column(db.String(150))
    quantity = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))
    
    def __repr__(self):
        return f'{self.name} - {self.rate} - {self.quantity}'
    
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_no = db.Column(db.Integer, nullable=False)
    invoice_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    due_date = db.Column(db.Date(), nullable=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    note = db.Column(db.Text())
    items = db.relationship('InvoiceItem', backref='invoice', lazy=True)
    labour = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'{self.invoice_no} - {self.items}'
    