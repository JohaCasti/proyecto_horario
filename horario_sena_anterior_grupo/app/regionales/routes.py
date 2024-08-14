from flask import render_template, flash,redirect
from flask_login import login_required
from app.regionales import regionales
import app
from .forms import NewRegionForm, EditRegionForm

@regionales.route('/createRegional',methods=['GET','POST'])
def crear():
    p = app.models.Regional()
    form = NewRegionForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect('/regionales/listarRegion')
    return render_template('new.html',
                           form=form)


@regionales.route('/listarRegion')
def listar():
     ## seleccionar los productos
    regionales = app.models.Regional.query.all()
    return render_template("regionales.html", 
                            regionales = regionales)  
 
@regionales.route('/editar/<id_Regional>',methods=['GET','POST'])
def editar (id_Regional):
    p = app.models.Regional.query.get(id_Regional)
    form = EditRegionForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Region actualizada')
        return redirect('/regionales/listarRegion')
    return render_template('new.html',
                           form=form)

@regionales.route('/eliminar/<id_Regional>')
def eliminar (id_Regional):
    p = app.models.Regional.query.get(id_Regional)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Regional eliminada')
    return redirect('/regionales/listarRegion')