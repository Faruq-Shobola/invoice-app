from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_required, current_user
from invoice import db
from invoice.invoice.forms import InvoiceForm
from invoice.models import Client, Invoice, InvoiceItem

invoice = Blueprint('invoice', __name__)


@invoice.route('/')
def invoices():
    return '<h1>All Invoices</h1>'


@invoice.route('/add-new', methods=['GET', 'POST'])
@login_required
def add_invoice():
    form = InvoiceForm()
    form.client.choices = [(client.id, client.name) for client in Client.query.filter_by(customer=current_user).order_by(Client.name).all()]    

    if form.validate_on_submit():
        try:
            client = form.client.data
            due_date = form.due_date.data
            note = form.note.data
            labour = form.labour.data
            
            invoice = Invoice(invoice_id=1, note=note, labour=labour)
            
            items = form.items.data
            for item in items:
                item_name = item['item_name']
                item_details = item['item_details']
                rate = item['rate']
                quantity = item['quantity']
                
                item = InvoiceItem(name=item_name, details=item_details, rate=rate, quantity=quantity)        
                invoice.items.append(item)        
        
            db.session.add(invoice)
            db.session.commit()
            
            flash('Invoice Added', 'info')
            return redirect(url_for('auth.home'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error {str(e)}', 'danger')           

    elif request.method == 'GET':
        pass
    
    return render_template('invoice/addinvoice.html', title='Invoice', form=form)