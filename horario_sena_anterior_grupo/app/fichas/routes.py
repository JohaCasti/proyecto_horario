from flask import render_template, flash,redirect
from flask_login import login_required, current_user
from app.fichas import fichas
import app
from .forms import NewFichaForm, EditFichaForm

#Metodo creación de fichas
@fichas.route('/createFicha',methods=['GET','POST'])
def crear():
    p = app.models.Ficha()
    form = NewFichaForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect('/fichas/listarFicha')
    return render_template('new_ficha.html', form=form)


#Metodo de listar fichas en la vista home
@fichas.route('/listarFicha')
def listar():
     ## seleccionar los productos
    fichas = app.models.Ficha.query.all()
    return render_template("fichas.html", 
                            fichas=fichas)  



 
#Metodo para editar Ficha por id
@fichas.route('/editar/<id_Ficha>',methods=['GET','POST'])
def editar (id_Ficha):
    p = app.models.Ficha.query.get(id_Ficha)
    form = EditFichaForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('fichas actualizado')
        return redirect('/fichas/listarFicha')
    return render_template('new_ficha.html',
                           form=form)

#Metodo para eliminar fichas por id
@fichas.route('/eliminar/<id_Ficha>')
def eliminar (id_Ficha):
    p = app.models.Ficha.query.get(id_Ficha)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Ficha eliminado')
    return redirect('/fichas/listarFicha')