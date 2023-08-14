from flask import Blueprint, render_template
from .forms import RegistrartionForm

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
  return "Hello World"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  form = RegistrartionForm()
  
  return render_template('sign_up.html', title='Sign up', form=form)


