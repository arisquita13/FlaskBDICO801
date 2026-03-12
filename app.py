from flask import Flask, render_template,request, redirect, url_for
import forms
from flask_wtf.csrf import CSRFProtect
from flask import flash
from config import DevelopmentConfig


from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf = CSRFProtect(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/usuarios",methods=["GET","POST"])
def usuario():
    usuarios_clas=forms.UserForm(request.form)
    
    if request.method=='POST':
        # Crear nuevo alumno y guardar en BD
        nuevo_alumno = Alumnos(
            nombre=usuarios_clas.nombre.data,
            apaterno=usuarios_clas.apaterno.data,
            amaterno=usuarios_clas.amaterno.data,
            email=usuarios_clas.correo.data,
            edad=usuarios_clas.edad.data
        )
        db.session.add(nuevo_alumno)
        db.session.commit()
        flash('Alumno guardado exitosamente!')
        return redirect(url_for('usuario'))
    
    # Obtener todos los alumnos de la BD
    alumnos = Alumnos.query.all()
    
    return render_template('usuarios.html', form=usuarios_clas, alumnos=alumnos)

if __name__ == '__main__':
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
 