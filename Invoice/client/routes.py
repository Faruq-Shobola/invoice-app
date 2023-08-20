import os
from flask import current_app
from flask import redirect, render_template, request, url_for, flash, Blueprint
from flask_login import login_required, current_user
from invoice import db
from invoice.client.forms import ClientForm
from invoice.models import Client
from invoice.utils import save_image, paginate

client = Blueprint('client', __name__)


@client.route('/')
@login_required
def clients():
    clients = Client.query.filter_by(customer=current_user).order_by(Client.date_joined.desc())
    clients = paginate(clients, 5)
    return render_template('client/clients.html', title='Clients', clients=clients, endpoint='client.clients')


@client.route('/add-new', methods=['GET', 'POST'])
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

@client.route('/<int:id>')
@login_required
def single_client(id):
    client = Client.query.get_or_404(id)
    return render_template('client/single-client.html', title='Client', client=client)
    

@client.route('/<int:id>/delete')
@login_required
def delete_client(id):
    client = Client.query.get_or_404(id)
    client_logo_path = os.path.join(current_app.root_path, 'static/images/client-img', client.logo) 
    os.unlink(client_logo_path)
    db.session.delete(client)
    db.session.commit()
    flash('Client successfully deleted', 'info')
    return redirect(url_for('client.clients'))


@client.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_client(id):
    client = Client.query.get_or_404(id)
    form = ClientForm()
    
    if form.validate_on_submit():
        client.name = form.name.data
        client.client_type = form.client_type.data
        client.email = form.email.data
        client.phone = form.number.data
        client.website = form.website.data
        if form.logo.data:
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images/client-img', client.logo) )
                client.logo = save_image(image=form.logo.data, folder='client-img')
            except:
                client.logo = save_image(image=form.logo.data, folder='client-img')
                
        client.address = form.address.data
        db.session.commit()
        flash('Client details has been updated','info')
        return redirect(url_for('client.single_client', id=client.id))
    
    elif request.method == 'GET':
        form.name.data = client.name 
        form.client_type.data = client.client_type
        form.email.data = client.email
        form.number.data = client.phone
        form.website.data = client.website
        form.address.data = client.address
        
    
    return render_template('/client/editclient.html', title='Edit Client', form=form)

