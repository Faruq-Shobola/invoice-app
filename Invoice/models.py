from invoice import db, login_manager
from flask import current_app
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    clients = db.relationship('Client', backref='customer', lazy=True)
    
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
    
    def __repr__(self):
        return f'{self.name} - {self.email}'