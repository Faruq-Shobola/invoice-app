from flask import render_template, Blueprint
from flask_login import login_required, current_user
from invoice.invoice.forms import InvoiceForm
from invoice.models import Client, Invoice, InvoiceItem

invoice = Blueprint('invoice', __name__)


@invoice.route('/')
def invoices():
    return '<h1>All invoice</h1>'

@invoice.route('/add-new', methods=['GET', 'POST'])
@login_required
def add_invoice():
    form = InvoiceForm()
    form.client.choices = [(client.id, client.name) for client in Client.query.filter_by(customer=current_user).order_by(Client.name).all()]

    if form.validate_on_submit():
        client = form.client.data
        invoice_date = form.invoice_date.data
        due_date = form.due_date.data
        note = form.note.data
        labour = form.labour.data
        
        items = form.items.data
        for item in items:
            item_name = item.item_name
            item_details = item.item_details
            rate = item.rate
            quantity = item.quantity
            
            item = InvoiceItem(name=item_name, details=item_details, rate=rate, quantity=quantity)
            
        invoice = Invoice(invoice_id=1, invoice_date=invoice_date, due_date=due_date, note=note, labour=labour)
        invoice.items.append(item)
        
        print(invoice)
        
        db.session.add(invoice)

    return render_template('invoice/addinvoice.html', title='Invoice', form=form)