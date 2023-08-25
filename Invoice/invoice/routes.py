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
    return render_template('invoice/addinvoice.html', title='Invoice', form=form)