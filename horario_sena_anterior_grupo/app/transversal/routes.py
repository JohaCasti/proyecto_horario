from flask import render_template, flash,redirect
from flask_login import login_required
from app.transversal import transversal
import app
from .forms import NewTransversalForm, EditTransversalForm

@transversal.route('/createTransversal',methods=['GET','POST'])
def crear():
    p = app.models.Transversal()
    form = NewTransversalForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect('/transversal/listarTransversal')
    return render_template('new.html',
                           form=form)


@transversal.route('/listarTransversal')
def listar():
     ## seleccionar los productos
    transversal = app.models.Transversal.query.all()
    return render_template("transversales.html", 
                            transversal = transversal)      


@transversal.route('/editar/<id_Transversal>',methods=['GET','POST'])
def editar (id_Transversal):
    p = app.models.Transversal.query.get(id_Transversal)
    form = EditTransversalForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Transversales actualizadas')
        return redirect('/transversal/listarTransversal')
    return render_template('new.html',
                           form=form)

@transversal.route('/eliminar/<id_Transversal>')
def eliminar (id_Transversal):
    p = app.models.Transversal.query.get(id_Transversal)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Transversal eliminada')
    return redirect('/transversal/listarTransversal')                                                   