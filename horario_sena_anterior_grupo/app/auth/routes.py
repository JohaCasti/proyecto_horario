from flask_login import login_user, logout_user, login_required
from flask import render_template,redirect,flash
from app.auth import auth 
from .forms import LoginForm
import app

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Seleccionar el usuario por nombre de usuario
        user = app.models.Administrador.query.filter_by(username=form.username.data).first()
        if user is None or user.password != form.password.data:
            flash('El usuario no existe o la contraseña es incorrecta')
            return redirect('/auth/login')
        else:
            login_user(user, remember=True)
            flash("Iniciaste sesión")
            return redirect('/centros/listarCentro')
    return render_template("login.html", form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash("Cierre de sesión exitoso")
    return redirect('/auth/login')