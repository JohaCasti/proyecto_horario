from flask import (
    Blueprint, render_template, request, url_for, redirect, flash, session, g
    )
from werkzeug.security import generate_password_hash, check_password_hash
from .models_db import Administrador
from project import db



auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/registro', methods = ('GET', 'POST'))
def register():
    if request.method == 'POST':
        nombre = request.form['name']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        tipo_admin = request.form['tipo_admin']
        username = request.form['username']
        password = request.form['password']

        # admin = Administrador(
        #     nombre, apellido, telefono, tipo_admin, username, 
        #     generate_password_hash(password))

        # error = None
        # user_a = Administrador.query.filter_by(Tipo_admin = tipo_admin).first()
        # if user_a == None:
        #     db.session.add(admin)
        #     db.session.commit()
        #     error = f'El usuario {nombre} {apellido} se registro correctamente'
        #     flash(error)
        #     return redirect(url_for('auth.logadmin'))
        # else:
        #     error = f'El usuario {nombre} {apellido} ya esta registrado'
        
        # flash(error)
        url = "http://127.0.0.1:5000/consultapi/regisadmin"
        api = request.get(url)
        data = api.json()
        print(data)
        

    return render_template('auth/register.html')


@auth.route('/login', methods = ('GET', 'POST'))
def logadmin():

    if request.method == 'POST':
        nombre = request.form['username']
        password = request.form['password']

        

        error = None
        user = Administrador.query.filter_by(Nombre = nombre).first()
        if   user == None:
            error = 'Nombre de usuario incorrecto'
        elif not check_password_hash(user.Password, password):
            error = 'Contraseña incorrecto'

        if error == None:
            session.clear()
            session['user_id'] = user.id_admin

            return redirect(url_for('admin.home'))
        

        flash(error)
    return render_template('auth/login.html')


@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user =  Administrador.query.get_or_404(user_id)
        
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