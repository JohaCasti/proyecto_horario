from flask import (
    Blueprint, render_template, request, url_for, redirect, flash, session, g,
    )
from werkzeug.security import generate_password_hash, check_password_hash
import requests



auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/registro', methods = ('GET', 'POST'))
def register():
    if request.method == 'POST':
        nombre = request.form['name']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        tipo_admin = request.form['tipo_admin']
        username = request.form['Emailadmin']
        password = request.form['password']

        payload = {
            'nombre': nombre, 'apellido': apellido, 'telefono': telefono,
              'tipo_admin': tipo_admin, 'username': username,
                'password': password
        }
        url = "http://127.0.0.1:8000/consult/regisadmin"
        consult = "http://127.0.0.1:8000/consult/especif/"
        useri = requests.get(consult+tipo_admin)
        user = useri.json()
        if user == None:
            api = requests.post(url, json=payload)
            if api.status_code == 200:
                mensaje = f'El usuario {nombre} {apellido} se registro correctamente'
                flash(mensaje)
            else:
                mensaje = "a ocurrido un problema.. intentelo de nuevo"
                flash(mensaje)
        else:
            mensaje = f'El usuario {nombre} {apellido} ya existe!!'
            flash(mensaje)

    return render_template('auth/register.html')


@auth.route('/login', methods = ('GET', 'POST'))
def logadmin():

    if request.method == 'POST':
        nombre = request.form['Emailadmin']
        password = request.form['password']

        consult = "http://127.0.0.1:8000/consult/espec/"
        useri = requests.get(consult+nombre+"/admin/Username")
        user = useri.json()
        print(user)
        if user == None or not check_password_hash(user[6], password):
            mensaje = "El usuario o contraseña son incorrectas."
            flash(mensaje)
        else: 
            session.clear()
            session['user_id'] = user[0]
            return redirect(url_for('admin.home'))
        

    return render_template('auth/login.html')


@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        print(user_id)
        consult = "http://127.0.0.1:8000/consult/especifid/"
        useri = requests.get(consult+user_id)
        user = useri.json()
        # g.user =  user_id.query.get_or_404(user_id)
        g.user = user[1]
        g.id = user[0]
        
@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# no permitir vistas fuera de logeo
import functools

def login_required(view):
    @functools.wraps(view)
    def permisos(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.logadmin'))
        return view(**kwargs)
    return permisos
