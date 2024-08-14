from flask import (
    Blueprint, render_template, request, url_for, redirect, session, flash
)
admin = Blueprint('admin', __name__, url_prefix='/admin')
import requests
from project.auth import login_required
from .models import Create
import time

@admin.route('/home', methods = ('GET', 'POST'))
@login_required
def home():
            
    return render_template('pages/index.html')


#vista centros
@admin.route('/centros', methods =['GET','POST'])
def todo_centro():
    #traer centros
    dats = Create()
    dat = dats.get('centro')

    if request.method == 'POST':
        nom = request.form['namecenter']
        tel = request.form['tel_center']
        descrip = request.form['des_center']
        # llamamos clase create y usamos el metodo de su creacion!
        centro = Create()
        centro.centros(nom, tel, descrip)
    
    
    return render_template('pages/centros.html', datos=dat)

#vista instructores
@admin.route('/instructores')
def todo_instructor():
    return render_template('pages/instructores.html')

#vista fichas
@admin.route('/fichas')
def todo_ficha():
    return render_template('pages/ficha.html')


@admin.route('/asignar', methods = ['GET','POST'])
@login_required
def asignar():
    # informacion 
    url = "http://127.0.0.1:8000/consult/colum/Nombre/centro"
    api = requests.get(url)
    datos = api.json()

    # cuando se envie el evento de agregar un horario
    if request.method == 'POST':

        start = request.form['Start']
        end = request.form['End']
        hori = request.form['Hora_ini']
        horaf = request.form['Hora_fin']
        cen = request.form['value']
        ins = request.form['value']
        sal = request.form['value']
        ficha = request.form['value']
        color = request.form['color']
        datos = request.form['datoss']
        if end == "":
            end = start

        horario = Create()
        horario.horarios(start, end, hori, horaf, cen, ins, sal, ficha, color, datos)
        

    return render_template('pages/asignar.html', datos = datos)


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
@admin.route('/editar/<int:id>/<int:obj>', methods = ['GET', 'POST', 'PUT'])
@login_required
def editar(id,obj):
    dato = id
    obj = obj

    edit = Create()
    datosC = edit.datos(str(id),'id_centro', 'centro')

    if request.method == 'POST':
        nom = request.form['namecenter']
        tel = request.form['tel_center']
        des = request.form['des_center']
        id= str(dato)
        edit.actualcen('centro',nom, tel, des, id)

        # return redirect(url_for('admin.todo_centro'))
        # time.sleep(4)
        
            

    return render_template('pages/editar.html', datos=datosC, obj=obj )

#eliminar 
@admin.route('/editar/<int:id>/<dat>/<tab>', methods = ['POST','DELETE'])
@login_required
def delete(id, dat, tab):
    borra = Create()
    borra.borrar()

    return render_template('pages/centros.html')

