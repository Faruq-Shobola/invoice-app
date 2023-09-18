from flask import redirect, render_template, url_for, Blueprint
from flask_login import login_required

acct = Blueprint('account', __name__)

@acct.route('/dashboard')
@login_required
def home():
    return render_template('account/dashboard.html', title='Dashboard')


@acct.route('/profile')
@login_required
def profile():
    return render_template('account/profile.html', title='Profile')