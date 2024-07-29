from flask import (
    Blueprint, render_template, request, url_for, redirect, session, flash
)
admin = Blueprint('admin', __name__, url_prefix='/admin')

from project.auth import login_required
from .models import Create

@admin.route('/home', methods = ('GET', 'POST'))
@login_required
def home():
    # enviamos dos parametros accion y el objeto
    if request.method == 'POST':
        dato = request.form['value']
        accion = request.form['accion']
        if dato and accion == 'crear':
            return redirect(url_for('admin.create', dato=dato, accion = accion))
        elif dato and accion == 'editar':
            return redirect(url_for('admin.editar', dato=dato, accion = accion))
        elif dato and accion == 'asignar':
            return redirect(url_for('admin.asignar', dato=dato, accion = accion))
        else:
            return redirect(url_for('admin.consultar'))
        
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
        
        if dato1 == 'centro':
            nom = request.form['namecenter']
            tel = request.form['tel_center']
            descrip = request.form['des_center']
        # llamamos clase create y usamos el metodo de su creacion!
            centro = Create()
            centro.centros(nom, tel, descrip)
        elif dato1 == 'instructor':
            nom = request.form['name_ins']
            ape = request.form['apellidos_ins']
            ide = request.form['identificacion']
            mail = request.form['correo_inst']
            tel = request.form['tel_ins']
            contra = request.form['contrato']
            horas = request.form['horasT']
            passwd = request.form['password']

            profe = Create()
            profe.instructores(nom, ape, ide, mail, tel, contra, horas, passwd)
        elif dato1 == 'salon':
            cen = request.form['centro']
            num = request.form['numficha']
            des = request.form['des_ficha']

            salon = Create()
            salon.salones(cen, num, des)
        elif dato1 == 'ficha':
            num = request.form['numficha']
            prog = request.form['programa']
            ins = request.form['profe_ficha']
            des = request.form['des_ficha']

            ficha = Create()
            ficha.fichas(num, prog, ins, des)
        else:
            pass # espacio para natalia

    
    return render_template('pages/create.html', dato1 = dato1, accion = accion)



#consulta
@admin.route('/consultar')
@login_required
def consultar():
    return render_template('pages/consultar.html')

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

