from flask import redirect, render_template, url_for, flash, Blueprint
from flask_login import login_required, current_user
from invoice import db
from invoice.client.forms import ClientForm
from invoice.models import Client
from invoice.utils import save_image

client = Blueprint('client', __name__)


@client.route('/clients')
@login_required
def clients():
    clients = Client.query.filter_by(customer=current_user).all()
    return render_template('client/clients.html', title='Clients', clients=clients)


@client.route('/add-client', methods=['GET', 'POST'])
@login_required
def add_client():
    form = ClientForm()
    if form.validate_on_submit():
        name = form.name.data
        client_type = form.client_type.data
        email = form.email.data
        phone = form.number.data
        website = form.website.data
        if form.logo.data: 
            logo = save_image(image=form.logo.data, folder='client-img')
        address = form.address.data
        client = Client(name=name, client_type=client_type, email=email, phone=phone, website=website, logo=logo, address=address, customer=current_user)
        db.session.add(client)
        db.session.commit()
        flash('New client added','info')
        return redirect(url_for('client.clients'))
        
    
    return render_template('/client/addclient.html', title='Add Client', form=form)

