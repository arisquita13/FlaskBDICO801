from wtforms import Form, StringField, IntegerField, RadioField, SubmitField, ValidationError

class TicketForm(Form):
    nombre = StringField('Nombre', [])
    cantidad = IntegerField('Cantidad', [])
    tarjeta_cineco = RadioField('Tarjeta Cineco', choices=[('si', 'Sí'), ('no', 'No')], default='no')
    submit = SubmitField('Procesar')

    def validate_cantidad(form, field):
        if field.data is None:
            raise ValidationError('La cantidad es requerida')
        if field.data < 1 or field.data > 7:
            raise ValidationError('máximo 7 boletos por persona')
        if field.data > 7:
            raise ValidationError('No puedes comprar más de 7 boletos')
