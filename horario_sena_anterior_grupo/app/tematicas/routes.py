from flask import render_template, flash,redirect
from flask_login import login_required, current_user
from app.tematicas import tematicas
import app
from .forms import NewTematicaForm, EditTematicaForm

#Metodo creación de tematicas
@tematicas.route('/createTematica',methods=['GET','POST'])
def crear():
    p = app.models.Tematica()
    form = NewTematicaForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect('/tematicas/listarTematicas')
    return render_template('new_tem.html', form=form)

#Metodo de listar tematicas en la vista home
@tematicas.route('/listarTematicas')
def listar():
    ## seleccionar los productos
    tematicas = app.models.Tematica.query.all()
    return render_template("tematicas.html", 
                            tematicas=tematicas)  

#Metodo para editar tematicas por id
@tematicas.route('/editar/<id_Tematica>',methods=['GET','POST'])
def editar (id_Tematica):
    p = app.models.Tematica.query.get(id_Tematica)
    form = EditTematicaForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('tematicas actualizadas')
        return redirect('/tematicas/listarTematicas')
    return render_template('new_tem.html', form=form)

#Metodo para eliminar tematicas por id
@tematicas.route('/eliminar/<id_Tematica>')
def eliminar (id_Tematica):
    p = app.models.Tematica.query.get(id_Tematica)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Tematica eliminada')
    return redirect('/tematicas/listarTematicas')