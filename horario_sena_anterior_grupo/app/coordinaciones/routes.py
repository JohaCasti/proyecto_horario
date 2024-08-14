from flask import render_template, flash,redirect, url_for
from app.coordinaciones import coordinaciones
import app
from .forms import NewCoordinacionForm, EditCoordinacionForm

@coordinaciones.route('/createCoordinacion',methods=['GET','POST'])
def crear():

    p = app.models.Coordinacion()
    form = NewCoordinacionForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect(url_for('coordinaciones.listar', Id_Centro=p.Id_Centro))
    return render_template('new_coor.html',
                           form=form)


@coordinaciones.route('/listarCoordinacion/<Id_Centro>')
def listar(Id_Centro):
     ## seleccionar los productos
     
    coordinacion = app.models.Coordinacion.query.filter_by(Id_Centro=Id_Centro).all() 
    return render_template("coordinaciones.html", 
                            coordinacion = coordinacion)      

@coordinaciones.route('/listarCoordinacion_home/<Id_Centro>')
def listar_home(Id_Centro):
     ## seleccionar los productos
    coordinacion = app.models.Coordinacion.query.filter_by(Id_Centro=Id_Centro).all()
    return render_template("home_coordinaciones.html", 
                            coordinacion = coordinacion)

#Metodo para editar centro por id
@coordinaciones.route('/editar/<id_Coordinacion>',methods=['GET','POST'])
def editar (id_Coordinacion):
    coordinacion = app.models.Coordinacion.query.get(id_Coordinacion)
    form = EditCoordinacionForm(obj = coordinacion)
    if form.validate_on_submit():
        form.populate_obj(coordinacion)
        app.db.session.commit()
        flash('Coordinacion actualizada')
        return redirect(url_for('coordinaciones.listar', Id_Centro=coordinacion.Id_Centro))
    return render_template('new_coor.html',
                           form=form)

@coordinaciones.route('/eliminar/<id_Coordinacion>')
def eliminar (id_Coordinacion):
    coordinacion = app.models.Coordinacion.query.get(id_Coordinacion)
    app.db.session.delete(coordinacion)
    app.db.session.commit()
    flash('Coordinacion eliminada')
    return redirect(url_for('coordinaciones.listar', Id_Centro=coordinacion.Id_Centro))                                                  