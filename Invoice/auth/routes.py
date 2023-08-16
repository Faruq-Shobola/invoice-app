from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from invoice import db, bcrypt
from invoice.auth.forms import RegistrationForm, LoginForm
from invoice.auth.models import User

auth = Blueprint('auth', __name__)


@auth.route('/')
def home():
    return render_template('index.html', title="Home page")


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('auth.home'))
    
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

    return render_template('signup.html', title='Sign up', form=form)


@auth.route('/signin', methods=['Get', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('auth.home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        password = bcrypt.check_password_hash(user.password, form.password.data)
        if user and password:
            login_user(user, remember=form.remember.data)
            next = request.args.get('next')
            return redirect(next) if next else redirect(url_for('acct.home'))
        
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('signin.html', title="Sign in", form=form)


@auth.route('/signout')
def signout():
    logout_user()
    flash('You have logged out successfully', 'info')
    return redirect(url_for('auth.home'))
    