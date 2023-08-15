from flask import Blueprint, render_template, redirect, url_for, flash
from invoice import db, bcrypt
from invoice.auth.forms import RegistrartionForm
from invoice.auth.models import User

auth = Blueprint('auth', __name__)


@auth.route('/')
def home():
    return render_template('index.html', title="Home page")


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = RegistrartionForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=email, username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('You have been registered', 'success')
        return redirect(url_for('auth.home'))

    return render_template('sign_up.html', title='Sign up', form=form)
