from flask import render_template, flash,redirect
from flask_login import login_required, current_user
from app.centros import centros
import app
from .forms import NewCentroForm, EditCentroForm

#Metodo creación de centros
@centros.route('/createCentro',methods=['GET','POST'])
def crear():
    p = app.models.Centro()
    form = NewCentroForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect('/centros/listarCentro')
    return render_template('new.html',
                           form=form)


#Metodo de listar centros en la vista home
@centros.route('/listarCentro')
@login_required
def listar():
     ## seleccionar los productos
    user = current_user
    centros = app.models.Centro.query.all()
    return render_template("home.html", 
                            centros=centros, user=user)  

#Metodo listar centros en vista para procesos del mismo modulo
@centros.route('/listarCentro_g')
def listar_g():
     ## seleccionar los productos
    centros = app.models.Centro.query.all()
    return render_template("centros.html", 
                            centros = centros)  


 
#Metodo para editar centro por id
@centros.route('/editar/<id_Centro>',methods=['GET','POST'])
def editar (id_Centro):
    p = app.models.Centro.query.get(id_Centro)
    form = EditCentroForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('centros actualizado')
        return redirect('/centros/listarCentro')
    return render_template('new.html',
                           form=form)

#Metodo para eliminar centros por id
@centros.route('/eliminar/<id_Centro>')
def eliminar (id_Centro):
    p = app.models.Centro.query.get(id_Centro)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('centro eliminado')
    return redirect('/centros/listarCentro')