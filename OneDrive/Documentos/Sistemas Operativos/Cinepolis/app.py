from flask import Flask, render_template, request, jsonify
import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cinepolis_secret_2026'

PRECIO_BOLETO = 12.0

def calcular_descuento(cantidad):
    if cantidad > 5:
        return 0.15
    elif cantidad >= 3:
        return 0.10
    else:
        return 0.0

def calcular_total(cantidad, tiene_cineco):
    descuento_cantidad = calcular_descuento(cantidad)
    subtotal = cantidad * PRECIO_BOLETO
    total_con_desc_cantidad = subtotal * (1 - descuento_cantidad)
    
    if tiene_cineco:
        total_con_desc_cantidad *= 0.9
    
    return round(total_con_desc_cantidad, 2)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['GET', 'POST'])
def procesar():
    form = forms.TicketForm(request.form)
    resultado = None
    error = None
    
    if request.method == 'POST' and form.validate():
        cantidad = form.cantidad.data
        tiene_cineco = form.tarjeta_cineco.data == 'si'
        
        if cantidad > 7:
            error = 'máximo 7 boletos por persona'
        elif cantidad < 1:
            error = 'Cantidad inválida'
        else:
            subtotal = cantidad * PRECIO_BOLETO
            descuento_porc = calcular_descuento(cantidad) * 100
            total = calcular_total(cantidad, tiene_cineco)
            
            resultado = {
                'nombre': form.nombre.data,
                'cantidad': cantidad,
                'subtotal': round(subtotal, 2),
                'descuento_porc': int(descuento_porc),
                'tiene_cineco': tiene_cineco,
                'total': total
            }
    
    return render_template('procesar.html', form=form, resultado=resultado, error=error)

if __name__ == '__main__':
    app.run(debug=True)
