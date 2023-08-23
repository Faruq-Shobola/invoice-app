from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField ,DateField, SelectField ,TextAreaField ,SubmitField, FieldList, FormField
from wtforms.validators import DataRequired


class InvoiceItemForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    item_details = StringField('Item Details')
    unit_price = DecimalField('Price', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])


class InvoiceForm(FlaskForm):
    client = SelectField('Client', validators=[DataRequired()], coerce=int)
    invoice_date = DateField('Date Created', DataRequired())
    due_date = DateField('Due Date', validators=[DataRequired()])
    items = FieldList(FormField(InvoiceItemForm), validators=[DataRequired()], min_entries=1)
    Note = TextAreaField('Note')
    submit = SubmitField('Generate Invoice')