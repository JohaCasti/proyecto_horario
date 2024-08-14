from flask import render_template, flash,redirect
from flask_login import login_required
from app.instructores import instructores
import app
from .forms import NewInstructorForm, EditInstructorForm

@instructores.route('/createInstructor',methods=['GET','POST'])
def crear():
    p = app.models.Instructor()
    form = NewInstructorForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect('/instructores/listarInstructores')
    return render_template('new_ins.html',
                           form=form)


@instructores.route('/listarInstructores')
def listar():
     ## seleccionar los productos
    instructores = app.models.Instructor.query.all()
    return render_template("instructores.html", 
                            instructores = instructores)      


@instructores.route('/editar/<id_Instructor>',methods=['GET','POST'])
def editar (id_Instructor):
    p = app.models.Instructor.query.get(id_Instructor)
    form = EditInstructorForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Instructores actualizados')
        return redirect('/instructores/listarInstructores')
    return render_template('new.html',
                           form=form)

@instructores.route('/eliminar/<id_instructor>')
def eliminar (id_instructor):
    p = app.models.Instructor.query.get(id_instructor)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Instructor eliminado')
    return redirect('/instructores/listarInstructores')                                                   