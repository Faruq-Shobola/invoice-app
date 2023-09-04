from flask import render_template, Blueprint
from flask_login import login_required
from invoice.invoice.forms import InvoiceForm

invoice = Blueprint('invoice', __name__)


@invoice.route('/')
def invoices():
    return '<h1>All invoice</h1>'

@invoice.route('/add-new')
@login_required
def add_invoice():
    form = InvoiceForm()
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
            
    return render_template('invoice/addinvoice.html', title='Invoice', form=form)