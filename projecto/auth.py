from flask import (
    Blueprint, render_template, request, url_for, redirect, flash, session, g,
    )
from werkzeug.security import check_password_hash
import requests

auth = Blueprint('auth', __name__, url_prefix='/auth')
auth.url = "http://127.0.0.1:8000/"
@auth.route('/registro', methods = ('GET', 'POST'))
def register():
    if request.method == 'POST':
        nombre = request.form['name']
        apellido = request.form['apellido']
        tipo_admin = request.form['tipo_admin']
        username = request.form['Emailadmin']
        password = request.form['password']

        payload = {
            'nombre': nombre, 'apellido': apellido,
              'tipo_admin': tipo_admin, 'username': username,
                'password': password
        }
        url = auth.url+"consult/regisadmin"
        consult = auth.url+"consult/datos/"
        useri = requests.get(consult+tipo_admin+"/Identificacion/Admin")
        user = useri.json()
        print(user)
        if user == None:
            api = requests.post(url, json=payload)
            if api.status_code == 200:
                mensaje = f'El usuario {nombre} {apellido} se registro correctamente'
                flash(mensaje, "success")
            else:
                mensaje = "a ocurrido un problema.. intentelo de nuevo"
                flash(mensaje, "info")
        else:
            mensaje = f'El usuario {nombre} {apellido} ya existe!!'
            flash(mensaje, "error")

    return render_template('auth/register.html')


@auth.route('/login', methods = ('GET', 'POST'))
def logadmin():

    if request.method == 'POST':
        nombre = request.form['Emailadmin']
        password = request.form['password']

        consult = auth.url+"consult/datos/"
        useri = requests.get(consult+nombre+"/Correo/Admin")
        print(useri)
        user = useri.json()
        print(user)
        if user == None or not check_password_hash(user[5], password):
            mensaje = "El usuario o contraseña son incorrectas."
            flash(mensaje, "error")
        else:
            session.clear()
            session['user_id'] = user[0]
            session['name'] = user[1]
            session['apelli'] = user[2]
            return redirect(url_for('admin.home'))


    return render_template('auth/login.html')

@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    user_name = session.get('name')
    user_ape = session.get('apelli')
    if user_id is None:
        g.user = None
    else:
        user_id = str(user_id)
        consult = auth.url+"consult/especifid/"
        useri = requests.get(consult+user_id)
        user = useri.json()
        # g.user =  user_id.query.get_or_404(user_id)
        # g.user = user[1]
        # g.lastName= user[2]
        # g.id = user[0]
        g.user = user_id
        g.name = user_name
        g.ape = user_ape


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
