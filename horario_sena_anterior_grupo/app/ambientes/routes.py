from flask import render_template, flash,redirect
from flask_login import login_required, current_user
from app.ambientes import ambientes
import app
from .forms import NewAmbienteForm, EditAmbienteForm

#Metodo creación de centros
@ambientes.route('/createAmbiente',methods=['GET','POST'])
def crear():
    p = app.models.Ambiente()
    form = NewAmbienteForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect('/ambientes/listarAmbiente')
    return render_template('new.html',
                           form=form)


#Metodo de listar centros en la vista home
@ambientes.route('/listarAmbiente')
def listar():
     ## seleccionar los productos
    ambientes = app.models.Ambiente.query.all()
    return render_template("ambiente.html", 
                            ambientes=ambientes)  


 
#Metodo para editar centro por id
@ambientes.route('/editar/<id_Ambiente>',methods=['GET','POST'])
def editar (id_Ambiente):
    p = app.models.Ambiente.query.get(id_Ambiente)
    form = EditAmbienteForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('ambientes actualizado')
        return redirect('/ambientes/listarAmbiente')
    return render_template('new.html',
                           form=form)

#Metodo para eliminar centros por id
@ambientes.route('/eliminar/<id_Ambiente>')
def eliminar (id_Ambiente):
    p = app.models.Ambiente.query.get(id_Ambiente)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('ambiente eliminado')
    return redirect('/ambientes/listarAmbiente')