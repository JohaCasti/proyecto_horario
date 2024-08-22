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
    instru = Create()
    profe = instru.sumall('instructor')
    hora = instru.sumall('Horarios')
    return render_template('pages/index.html', pro=profe, hora=hora)


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


#vista sedes
@admin.route('/sedes')
def todo_sedes():
    return render_template('pages/sedes.html')

#vista programas
@admin.route('/programas', methods =['GET','POST'])
def todo_programas():
    program = Create()
    cen = program.get('centro')
    #traer datos escalados por tablas con join
    dat = program.getJoin('programas','centro', 'centro','id_centro')

    if request.method == 'POST':
        nom = request.form['nomProgram']
        des = request.form['programDes']
        cen = request.form['programCentro']
        program.programa(nom, des, cen)

    cen = program.get('centro')
    dat = program.getJoin('programas','centro', 'centro','id_centro')
    
    return render_template('pages/programas.html', datos = dat, cen=cen)


#vista instructores
@admin.route('/instructores')
def instructor():
    return render_template('pages/instructores.html')

#vista instructores
@admin.route('/salones')
def todo_salones():
    return render_template('pages/salones.html')

#vista fichas
@admin.route('/fichas')
def ficha():
    fichas = Create()
    fich = fichas.get('ficha')
    inst = fichas.get('instructor')
    prog = fichas.get('programas')
    list = fichas.getJoinDual('ficha','programas', 'instructor','programa','id_programa','instructor','id_instructor')



    return render_template('pages/ficha.html', fich=fich, ins=inst, prog=prog, list=list)

@admin.route('/asignar', methods = ['GET','POST'])
@login_required
def asignar():
    # traer informacion 
    datos = Create()
    dath = datos.get('Horarios')
    datc = datos.get('centro')
    dati = datos.get('instructor')

    # cuando se envie el evento de agregar un horario
    if request.method == 'POST':

        start = request.form['Start']
        end = request.form['End']
        hori = request.form['Hora_ini']
        horaf = request.form['Hora_fin']
        cen = request.form['centro']
        prom = request.form['programa']
        ins = request.form['instructor']
        sal = request.form['salon']
        ficha = request.form['fichas']
        color = request.form['colorH']
        datos = request.form['datoss']
        if end == "":
            end = start

        horario = Create()
        horario.horarios(start, end, hori, horaf, cen, ins, sal, ficha, color, datos)
        
        

    return render_template('pages/asignar.html', hor=dath, centros=datc, profed=dati)


# crear
@admin.route('/create/ficha')
@admin.route('/create/salon')
@admin.route('/create/instructor')
@admin.route('/create/centro')
@admin.route('/create', methods = ['GET','POST'])
@login_required
def reserva():
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
    datosP = edit.datos(str(id), 'id_programa', 'programas')
    selCentro = edit.get('centro')
    joinPro = edit.joinUnDate('Nombre', 'programas', 'centro', 'centro','id_centro', str(dato),'id_programa')
    if request.method == 'POST':
        if obj == 1:
            nom = request.form['namecenter']
            tel = request.form['tel_center']
            des = request.form['des_center']
            id= str(dato)
            edit.actualcen('centro',nom, tel, des, id)

            # return redirect(url_for('admin.todo_centro'))
            # time.sleep(4)
        elif obj == 2:
            pass
        elif obj == 3:
            pass
        elif obj == 4:
            pass
        elif obj == 5:
            nom = request.form['nomProgram']
            tel = request.form['programDes']
            des = request.form['programCentro']
            id= str(dato)
            edit.actualpro('programas',nom, tel, des, id)
        else :
            pass
    # mostrar datos actualizados al instante
    datosC = edit.datos(str(id),'id_centro', 'centro')  
    datosP = edit.datos(str(id), 'id_programa', 'programas')

    return render_template('pages/editar.html', datos=datosC, obj=obj, datosp=datosP, cen = selCentro, cenpro=joinPro)

#eliminar 
@admin.route('/editar/<id>/<dat>/<tab>', methods = ['GET', 'POST','DELETE'])
@login_required
def delete(id, dat, tab):
    if request.method == 'POST':
        # id = request.form['value']
        borra = Create()
        borra.borrar(tab, dat, id)

    return render_template('pages/centros.html')

