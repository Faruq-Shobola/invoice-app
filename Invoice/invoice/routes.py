from flask import Blueprint

invoice = Blueprint('invoice', __name__)


@invoice.route('/')
def invoices():
    return '<h1>All invoice</h1>'

@invoice.route('/add-new')
def add_invoice():
    return '<h1>Add New invoice</h1>'