from flask import redirect, render_template, url_for, flash, Blueprint
from invoice.client.forms import ClientForm

client = Blueprint('client', __name__)


@client.route('/add-client', methods=['GET', 'POST'])
def add_client():
    form = ClientForm()
    
    return render_template('/client/addclient.html', title='Add Client', form=form)