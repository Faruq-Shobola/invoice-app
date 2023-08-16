from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from invoice import db, bcrypt
from invoice.auth.forms import RegistrationForm, LoginForm, PasswordResetRequestForm, PasswordResetForm
from invoice.auth.models import User
from invoice.mailgun import MailgunApi
from dotenv import load_dotenv
import os


auth = Blueprint('auth', __name__)

load_dotenv()

mailgun = MailgunApi(domain=os.getenv('MAILGUN_DOMAIN'), api_key=os.getenv('MAILGUN_API_KEY'))


@auth.route('/')
def home():
    return render_template('index.html', title="Home page")


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('account.home'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=email, username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('You have been registered', 'success')
        return redirect(url_for('auth.signin'))

    return render_template('auth/signup.html', title='Sign up', form=form)


@auth.route('/signin', methods=['Get', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('account.home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        password = bcrypt.check_password_hash(user.password, form.password.data)
        if user and password:
            login_user(user, remember=form.remember.data)
            next = request.args.get('next')
            return redirect(next) if next else redirect(url_for('account.home'))
        
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('auth/signin.html', title="Sign in", form=form)


@auth.route('/signout')
def signout():
    logout_user()
    flash('You have logged out successfully', 'info')
    return redirect(url_for('auth.home'))


@auth.route('/reset-password', methods=['GET', 'POST'])
def password_reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('account.home'))
    form = PasswordResetRequestForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        
        token = user.generate_reset_token()
        link = url_for('auth.password_reset', token=token, _external=True)
        text = f'It seems like you forgot your password. If this is true, click the link to reset your password. {link}'
        subject = 'Password Reset'
        mailgun.send_email(to=user.email, subject=subject, text=text, html=render_template('email/password-reset.html', link=link))

        flash('An email with instructions to reset your password has been sent to you.','info')
        
    return render_template('auth/password-reset-request.html', title='Password reset', form=form)
    

@auth.route('/reset-password/<string:token>', methods=['GET', 'POST'])
def password_reset(token):
    if current_user.is_authenticated:
        return redirect(url_for('account.home'))
    
    user = User.verify_reset_token(token)
    if not user:
        flash('That is an Invalid or expired token', 'warning')
        return redirect(url_for('auth.password_reset_request'))
    form = PasswordResetForm()
    if form.validate_on_submit():    
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been reset, you can Signin now','info')
        return redirect(url_for('auth.signin'))
        
    return render_template('auth/password-reset.html', title='Password reset', form=form)