from flask import render_template, flash,redirect, url_for
from app.programas import programas
import app
from .forms import NewProgramaForm, EditProgramaForm

@programas.route('/createPrograma',methods=['GET','POST'])
def crear():
    p = app.models.Programa()
    form = NewProgramaForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect(url_for('programas.listar', Id_Coordinacion=p.Id_Coordinacion))
    return render_template('new_pro.html',
                           form=form)


@programas.route('/listarPrograma/<Id_Coordinacion>')
def listar(Id_Coordinacion):
     ## seleccionar los productos
    programas = app.models.Programa.query.filter_by(Id_Coordinacion=Id_Coordinacion).all()
    return render_template("programas.html", 
                            programas = programas)      

@programas.route('/listarPrograma_home/<Id_Coordinacion>')
def listar_home(Id_Coordinacion):
     ## seleccionar los productos
    programas = app.models.Programa.query.filter_by(Id_Coordinacion=Id_Coordinacion).all()
    return render_template("programas_home.html", 
                            programas = programas)

#Metodo para editar centro por id
@programas.route('/editar/<id_Programa>',methods=['GET','POST'])
def editar (id_Programa):
    programa = app.models.Programa.query.get(id_Programa)
    form = EditProgramaForm(obj = programa)
    if form.validate_on_submit():
        form.populate_obj(programa)
        app.db.session.commit()
        flash('programa actualizado')
        return redirect(url_for('programas.listar', Id_Coordinacion=programa.Id_Coordinacion))
    return render_template('new.html',
                           form=form)

@programas.route('/eliminar/<id_Programa>')
def eliminar (id_Programa):
    programa = app.models.Programa.query.get(id_Programa)
    app.db.session.delete(programa)
    app.db.session.commit()
    flash('programa eliminada')
    return redirect(url_for('programas.listar', Id_Coordinacion=programa.Id_Coordinacion))                                                  