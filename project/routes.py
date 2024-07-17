from flask import (
    Blueprint, render_template, request, url_for, redirect, session, flash
)
admin = Blueprint('admin', __name__, url_prefix='/admin')

from project.auth import login_required
from .models_db import Centro
from project import db

@admin.route('/home', methods = ('GET', 'POST'))
@login_required
def home():
    if request.method == 'POST':
        dato = request.form['value']
        accion = request.form['accion']
        if dato and accion == 'crear':
            return redirect(url_for('admin.create', dato=dato, accion = accion))
        elif dato and accion == 'editar':
            return redirect(url_for('admin.editar', dato=dato, accion = accion))
        elif dato and accion == 'consultar':
            return redirect(url_for('admin.consultar', dato=dato, accion = accion))
        else:
            return redirect(url_for('admin.asignar', dato=dato, accion = accion))
        
    return render_template('pages/index.html')

@admin.route('/asignar')
@login_required
def asignar():
    
    return "Vista de asignación"


# crear
@admin.route('/create/ficha')
@admin.route('/create/salon')
@admin.route('/create/instructor')
@admin.route('/create/centro')
@admin.route('/create', methods = ['GET','POST'])
@login_required
def create():
    accion = request.args.get('accion')
    dato1 = request.args.get('dato')

    if request.method == 'POST':
        nombre = request.form['namecenter']
        telefono = request.form['tel_center']
        descripcion = request.form['des_center']

        centro = Centro (
            nombre, telefono, descripcion
        )
        aviso = None
        peti = Centro.query.filter_by(Nombre = nombre).first()
        if peti == None:
            db.session.add(centro)
            db.session.commit()
            aviso = f'El centro {nombre} fue creado exitosamente!!!'
            flash(aviso)
            return redirect(url_for('admin.create'))
        else:
            aviso = f'El centro {nombre} ya existe'
        flash(aviso)
    
    return render_template('pages/create.html', dato1 = dato1, accion = accion)



#consulta
@admin.route('/consultar')
@login_required
def consultar():
    return "Vista para ver los horarios consultarlos"

# editar
@admin.route('/editar/instructor')
@admin.route('/editar/centro')
@admin.route('/editar/ficha')
@admin.route('/editar/salon')
@admin.route('/editar/<dato>', methods = ['GET'])
@login_required
def editar():
    accion = request.args.get('accion')
    dato1 = request.args.get('dato1')
    return render_template('pages/editar.html', dato1 = dato1, accion = accion)

