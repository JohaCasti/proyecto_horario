from flask import render_template, flash,redirect, url_for
from app.horarios import horarios
import app
from .forms import NewHorarioForm, EditHorarioForm

@horarios.route('/createHorario',methods=['GET','POST'])
def crear():
    p = app.models.Horario()
    form = NewHorarioForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect(url_for('horarios.listar', Id_Programa=p.Id_Programa))
    return render_template('new_Horario.html', form=form)


@horarios.route('/listarHorario/')
def listar():
    ## seleccionar los productos
    horarios = app.models.Horario.query.filter_by().all()
    return render_template("horarios.html", 
                            horarios = horarios)      

@horarios.route('/listarHorario_home/<Id_Programa>')
def listar_home(Id_Programa):
    ## seleccionar los productos
    horarios = app.models.Horario.query.filter_by(Id_Programa=Id_Programa).all()
    return render_template("horarios_home.html", 
                            horarios = horarios )

#Metodo para editar centro por id
@horarios.route('/editar/<id_Horario>',methods=['GET','POST'])
def editar (id_Horario):
    Horarios = app.models.Horario.query.get(id_Horario)
    form = EditHorarioForm(obj = Horarios)
    if form.validate_on_submit():
        form.populate_obj(Horarios)
        app.db.session.commit()
        flash('horario actualizado')
        return redirect(url_for('horarios.listar', Id_Horario=Horarios.id_Horario))
    return render_template('new.html', form=form)

@horarios.route('/eliminar/<id_Horario>')
def eliminar (id_Horario):
    horarios = app.models.Horario.query.get(id_Horario)
    app.db.session.delete(horarios)
    app.db.session.commit()
    flash('programa eliminada')
    return redirect(url_for('horarios.listar', Id_Horario=horarios.Id_Programa))       