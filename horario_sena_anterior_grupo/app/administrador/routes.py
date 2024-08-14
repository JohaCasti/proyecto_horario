from flask import render_template, flash, redirect, request
from flask_login import login_required, current_user
from app.administrador import administrador
import app
from .forms import NewAdminForm, EditAdminForm


@administrador.route('/createAdmin', methods=['GET', 'POST'])
def crear():
    form = NewAdminForm(request.form)
    code_v = "E2JYL98"
    
    if request.method == 'POST' and form.code.data == code_v and form.validate():
        p = app.models.Administrador()
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        
        # Verifica si el usuario está autenticado después de agregar el administrador
        if current_user.is_authenticated:
            return redirect('/administrador/listarAdmins')
        else:
            return redirect('/auth/login')
    return render_template('new_adm.html', form=form)


@administrador.route('/listarAdmins')
def listar():
     ## seleccionar los productos
    administrador = app.models.Administrador.query.all()
    return render_template("administradores.html", 
                            administrador = administrador)  
 
@administrador.route('/editar/<id_administrador>',methods=['GET','POST'])
def editar (id_administrador):
    p = app.models.Administrador.query.get(id_administrador)
    form = EditAdminForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Administrador actualizado')
        return redirect('/administrador/listarAdmins')
    return render_template('new.html',
                           form=form)

@administrador.route('/eliminar/<id_administrador>')
def eliminar (id_administrador):
    p = app.models.Administrador.query.get(id_administrador)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Administrador eliminado')
    return redirect('/administrador/listarAdmins')