from flask import (
    Blueprint, render_template, request, url_for, redirect, session, flash, g
)
import requests
import openpyxl
from .models import Create
from projecto.auth import login_required
admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/home', methods = ('GET', 'POST'))
@login_required
def home():
    info = Create()
    profes = info.sumall('Instructores')
    centros = info.sumall('Centros')
    fichas = info.sumall('Fichas')
    print(centros)
    return render_template('pages/index.html', profes=profes, centros=centros, fichas=fichas)
#vista centros
@admin.route('/centros', methods =['GET','POST'])
@login_required
def centro():
    #traer centros
    datos = Create()
    dat = datos.get('Centros')

    if request.method == 'POST':
        nom = request.form['namecenter']
        tel = request.form['tel_center']
        descrip = request.form['des_center']
        # llamamos clase create y usamos el metodo de su creacion!
        datos.centros(nom, tel, descrip)
        
    #volver a cargar los cambios nuevos
    dat = datos.get('Centros')
    
    return render_template('pages/centros.html', datos=dat)

@admin.route('/sedes', methods =['GET','POST'])
@login_required
def sedes():
    datos = Create()
    dat = datos.getJoin('Sedes', 'Centros', 'id_centro', 'ID_centro')
    cen = datos.get('Centros')
    if request.method == 'POST':
        cen = request.form['Scentro']
        nom = request.form['Snombre']
        descrip = request.form['Sdes']
        datos.sedes(cen, nom, descrip)
    #volver a cargar los cambios nuevos
    dat = datos.getJoin('Sedes', 'Centros', 'id_centro', 'ID_centro')

    return render_template('pages/sedes.html', datos=dat, centros=cen)

@admin.route('/ambientes', methods =['GET','POST'])
@login_required
def ambientes():
    datos = Create()
    dat = datos.casJoin('Ambientes')
    cen = datos.get('Centros')
    if request.method == 'POST':
        sede = request.form['Ssedes']
        nom = request.form['Snombre']
        horas = request.form['Shoras']
        descrip = request.form['Sdes']
        datos.ambientes(sede, nom, horas, descrip)
    dat = datos.casJoin('Ambientes')
    return render_template('pages/ambientes.html', centros=cen, datos=dat)                   
@admin.route('/programas', methods =['GET','POST'])
@login_required
def programas():
    datos = Create()
    dat = datos.getJoin('Programas', 'Sedes', 'id_sede', 'ID_sedes') # trae los programas ya creados pa mostrar
    cen = datos.get('Centros') # trae los centros para seleccionar centros en el form
    grado = datos.get('Titulaciones') # trae las titulaciones para seleccionar titulo en el form
    if request.method == 'POST':
        sede = request.form['Psedes']
        progra = request.form['Pnombre']
        titulo = request.form['Ptitulo']
        descri = request.form['Pdes']
        datos.programas(sede, progra, titulo, descri)
    dat = datos.getJoin('Programas', 'Sedes', 'id_sede', 'ID_sedes')
    return render_template('pages/programas.html', datos=dat, centros=cen, grados=grado)

@admin.route('/fichas', methods =['GET','POST'])
@login_required
def fichas():
    datos = Create()
    dat = datos.casJoin('Fichas')
    cen = datos.get('Centros')
    #crear datos pa listar con join!! tarea pendiente
    if request.method == 'POST':
        progra = request.form['Fprogramas']
        ficha = request.form['numficha']
        descri = request.form['Fdes']
        datos.fichas(progra, ficha, descri)
    dat = datos.casJoin('Fichas')
    return render_template('pages/fichas.html', datos=dat, centros=cen)

@admin.route('/actividades', methods =['GET','POST'])
@login_required
def actividades():
    datos = Create()
    dat = datos.casJoin('Actividades')
    cen = datos.get('Centros')
    if request.method == 'POST':
        progra = request.form['Aprogramas']
        nombre = request.form['Anombre']
        horas = request.form['Ahoras']
        descri = request.form['Ades']
        datos.actividades(progra, nombre, horas, descri)
    dat = datos.casJoin('Actividades')
    return render_template('pages/actividades.html', datos=dat, centros=cen)

@admin.route('/docentes', methods =['GET','POST'])
@login_required
def docentes():
    datos = Create()
    dat = datos.get('Instructores')
    cen = datos.get('Centros')
    if request.method== 'POST':
        centro = request.form['Icentro']
        nombre = request.form['Inombre']
        apellidos = request.form['Iapellido']
        identi = request.form['Iidenti']
        correo = request.form['Imail']
        contra = request.form['Icontra']
        horas = request.form['Ihoras']
        paswd = request.form['Ipaswd']
        datos.docentes(centro, nombre, apellidos, identi, correo, contra, horas, paswd)

    return render_template('pages/instructores.html', datos=dat, centros=cen)

@admin.route('/carga/<id>', methods =['GET','POST'])
@login_required
def carga_masiva(id):
    datos = Create()
    dat = datos.get('Centros')
    id=id
    print(id)
    #vovler interables con un if dependiendo de su tabla para carga masiva!! tarea pendiente
    if request.method == 'POST':
        if id == '1':
            archivo= request.form['carga']
            datos.carga(archivo, "Centros")
        elif id == '2':
            archivo= request.form['carga']
            datos.carga_id(archivo, "Sedes", "Centro", "Centros")
        elif id == '3':
            archivo= request.form['carga']
            datos.carga_id(archivo, "Ambientes", "Sede", "Sedes")
        elif id == '4':
            archivo= request.form['carga']
            datos.carga_id(archivo, "Programas", "Sede", "Sedes")
        elif id == '5':
            archivo= request.form['carga']
            datos.carga_id(archivo, "Instructores", "Centro", "Centros")
        elif id == '6':
            archivo= request.form['carga']
            datos.carga_id(archivo, "Fichas", "Programa", "Programas")
        elif id == '7':
            archivo= request.form['carga']
            datos.carga_id(archivo, "Actividades", "Programa", "Programas")
    dat = datos.get('Centros')
    return render_template('pages/carga_masiva.html', datos=dat)

@admin.route('/perfil', methods =['GET','POST'])
@login_required
def perfil():
    datos = Create()
    id = g.user
    info = datos.datos(id, 'ID_admin', 'Admin')
    return render_template('pages/perfil.html', info=info)

@admin.route('/bloque', methods =['GET','POST'])
@login_required
def bloque():
    datos = Create()
    horarios = datos.get('Bloques')
    cen = datos.get('Centros')

    if request.method == 'POST':

        centro = request.form['Bcentro']
        sed = request.form['Bsede']
        prom = request.form['Bprogramas']
        ins = request.form['Bprofes']
        sal = request.form['Bambientes']
        ficha = request.form['Bfichas']
        acti = request.form['Bmateria']
        start = request.form['Start']
        end = request.form['End']
        hori = request.form['BhoraI']
        horaf = request.form['BhoraF']
        datos = request.form['Fdes']
        if end == "":
            end = start
        # conversion de tiempo a minutos
        print(hori)
        print(horaf)
        tiempo = Create()
        minI = tiempo.convertir(hori)
        minF = tiempo.convertir(horaf)
        minff = minF - 1
        print(minff)
        tiempo_clas = minF - minI
        # cuantas horas diarias
        hora_clas = tiempo_clas / 60
        print(hora_clas)
        try:
            num_dias = int(request.form['numDays'])
            horas_diarias = int(hora_clas)
            fecha_inicio = start
            fecha_final = end

            # Obtener los días seleccionados
            dias_seleccionados = []
            for i in range(1, num_dias + 1):
                dia_key = f'days{i}'
                if dia_key in request.form:
                    dias_seleccionados.append(int(request.form[dia_key]))

            # Verificar los datos recibidos
            if not dias_seleccionados or len(dias_seleccionados) != num_dias:
                flash("Error: No se seleccionaron los días correctamente.")
                return redirect(url_for('index'))

            # Procesar los datos (imprimir como ejemplo)
            print(f"Número de días: {num_dias}")
            print(f"Días seleccionados: {dias_seleccionados}")
            print(f"Horas diarias: {horas_diarias}")
            print(f"Fecha inicial: {fecha_inicio}")
            print(f"Fecha final: {fecha_final}")
            flash("Formulario procesado con éxito!")
        

        except Exception as e:
            flash(f"Hubo un error al procesar el formulario: {str(e)}")

        
        horario = Create()
        horario.horarios(centro, sed, prom, ins, sal, ficha, acti, start, end, minI, minff, datos, horas_diarias, dias_seleccionados)
    return render_template('pages/bloques.html', centros=cen)

@admin.route('/editar/<id>/<obj>', methods =['GET','POST'])
@login_required
def editar(id, obj):
    dato = id
    obj = int(obj)
    edit = Create()
    # cargar datos pa mostrar en los input´s
    datosC = edit.datos(id,'ID_centro', 'Centros')
    datosS = edit.joinDos('ID_centro', 'Centro', 'Sedes', 'Centros', 'id_centro', 'ID_centro', 'ID_sedes', id)
    datosI = edit.joinDos('ID_centro', 'Centro', 'Instructores', 'Centros', 'id_centro', 'ID_centro', 'ID_instructores', id)
    datosA = edit.joinTres('Centro', 'Sede', 'Ambientes', 'Sedes', 'id_sede', 'ID_sedes', 'Centros', 'id_centro', 'ID_centro', 'ID_ambiente', id)
    datosP = edit.joinCua('ID_sedes', 'Sede', 'ID_centro', 'Centro', 'ID_titulo', 'Titulacion', 'Programas', 'Sedes', 'id_sede', 'Centros', 'id_centro', 'Titulaciones', 'i','id_titulacion', 'ID_programa', id)
    datosF = edit.joinCua('ID_programa', 'Programa','ID_sedes', 'Sede', 'ID_centro', 'Centro', 'FIchas', 'Programas', 'id_programa', 'Sedes', 'id_sede', 'Centros', 's','id_centro', 'ID_ficha', id)
    datosM= edit.joinCua('ID_programa', 'Programa','ID_sedes', 'Sede', 'ID_centro', 'Centro', 'Actividades', 'Programas', 'id_programa', 'Sedes', 'id_sede', 'Centros', 's','id_centro', 'ID_actividades', id)
    selCentro = edit.get('Centros')
    grado = edit.get('Titulaciones')
    perfil = edit.datos(id, 'ID_admin', 'Admin')
    if obj == 1:
        #centro
        if request.method == 'POST':
            nom = request.form['namecenter']
            tel = request.form['tel_center']
            des = request.form['des_center'] 
            id= dato
            edit.actualcen('Centros', 'Centro', 'Telefono', 'Descripcion', 'ID_centro', nom, tel, des, id)

                # return redirect(url_for('admin.todo_centro'))
                # time.sleep(4)
    elif obj == 2:
        # instructor
        if request.method == 'POST':
            centro = request.form['Icentro']
            nombre = request.form['Inombre']
            apellidos = request.form['Iapellido']
            identi = request.form['Iidenti']
            correo = request.form['Imail']
            contra = request.form['Icontra']
            horas = request.form['Ihoras']
            id= str(dato)
            print(id)
            print("id profesor")
            edit.actualin(centro, nombre, apellidos, identi, correo, contra, horas, id)
    elif obj == 3:
        #actividades
        if request.method == 'POST':
            progra = request.form['Aprogramas']
            nombre = request.form['Anombre']
            horas = request.form['Ahoras']
            descri = request.form['Ades']
            id= str(dato)
            edit.actualacti(progra, nombre, horas, descri, id)
            #edit.actualact('Actividades', 'id_programa', 'Actividad', 'HorasTotal', 'ID_actividades', 'Descripcion', progra, nombre, horas, descri, id)
    elif obj == 4:
        # sedes
        if request.method == 'POST':
            cen = request.form['Scentro']
            nom = request.form['Snombre']
            descrip = request.form['Sdes']
            id= str(dato)
            edit.actualsed(cen, nom, descrip, id)
    elif obj == 5:
        # ambientes
        if request.method == 'POST':
            sede = request.form['Ssedes']
            nom = request.form['Snombre']
            horas = request.form['Shoras']
            descrip = request.form['Sdes']
            id= str(dato)
            edit.actualambi(sede, nom, horas, descrip, id)
            # no funciona no se porque
    elif obj == 6:
        # programas
        if request.method == 'POST':
            sede = request.form['Psedes']
            progra = request.form['Pnombre']
            titulo = request.form['Ptitulo']
            descri = request.form['Pdes']
            id= str(dato)
            edit.actualpro(sede, progra, titulo, descri, id)
    elif obj == 7:
        # fichas
        if request.method == 'POST':
            progra = request.form['Fprogramas']
            ficha = request.form['numficha']
            descri = request.form['Fdes']
            id = str(dato)
            edit.actualfich(progra, ficha, descri, id)
    elif obj == 8:
        # perfil admin
        if request.method == 'POST':
            nombre = request.form['ADMname']
            apellido = request.form['ADMape']
            identi = request.form['ADMdoc']
            correo = request.form['ADMmail']
            id= str(dato)
            print(id)
            edit.actualper(nombre, apellido, identi, correo, id)
    else :
        pass
    datosC = edit.datos(id,'ID_centro', 'Centros')
    datosS = edit.joinDos('ID_centro', 'Centro', 'Sedes', 'Centros', 'id_centro', 'ID_centro', 'ID_sedes', id)
    datosI = edit.joinDos('ID_centro', 'Centro', 'Instructores', 'Centros', 'id_centro', 'ID_centro', 'ID_instructores', id)
    datosA = edit.joinTres('Centro', 'Sede', 'Ambientes', 'Sedes', 'id_sede', 'ID_sedes', 'Centros', 'id_centro', 'ID_centro', 'ID_ambiente', id)
    datosP = edit.joinCua('ID_sedes', 'Sede', 'ID_centro', 'Centro', 'ID_titulo', 'Titulacion', 'Programas', 'Sedes', 'id_sede', 'Centros', 'id_centro', 'Titulaciones', 'i','id_titulacion', 'ID_programa', id)
    datosF = edit.joinCua('ID_programa', 'Programa','ID_sedes', 'Sede', 'ID_centro', 'Centro', 'FIchas', 'Programas', 'id_programa', 'Sedes', 'id_sede', 'Centros', 's','id_centro', 'ID_ficha', id)
    datosM= edit.joinCua('ID_programa', 'Programa','ID_sedes', 'Sede', 'ID_centro', 'Centro', 'Actividades', 'Programas', 'id_programa', 'Sedes', 'id_sede', 'Centros', 's','id_centro', 'ID_actividades', id)
    perfil = edit.datos(id, 'ID_admin', 'Admin')
    return render_template('pages/editar.html', obj=obj, centros=selCentro, datosC=datosC, datosS=datosS, datosA=datosA, datosP=datosP, grados=grado, datosF=datosF, datosM=datosM, datosI=datosI, perfil=perfil)

@admin.route('/descarga', methods =['GET','POST'])
@login_required
def descargas():
    if request.method == 'POST':
        tab = request.form['excelTab']
        dat = request.form['excelB']
        filtro = Create()
        if tab == 'Instructores':
            try:
                arr1 = filtro.excelIns(dat, 'ID_instructores', tab)
                #unicos = filtro.valores_unicos(arr1, 3)
                # creacion del excel
                excel = openpyxl.Workbook()
                sheet = excel.active
                sheet['A1'] = "Profesor:"
                sheet['B1'] = arr1[0][0]
                sheet['C1'] = arr1[0][1] 

                sheet['B3'] = "DOCENTE" 
                sheet['C3'] = "" 
                sheet['D3'] = "FECHA"
                sheet['E3'] = "DIA" 
                sheet['F3'] = "HORA" 
                sheet['G3'] = "FICHA"

                for index, row in enumerate(arr1):
                    sheet[f'B{index+4}'] = row[0]                       
                    sheet[f'C{index+4}'] = row[1]                       
                    sheet[f'D{index+4}'] = row[2]                       
                    sheet[f'E{index+4}'] = row[3]   
                    sheet[f'F{index+4}'] = str(row[4])+' am'+" - "+str(row[5])+' am'
                    sheet[f'G{index+4}'] = row[6]   
                excel.save("horario_1.xlsx")
                mensaje = "el excel se genero correctamente"
                flash(mensaje)
            except:
                print('hay un error con los datos para generar excel', 'danger')
                flash('hay un error con los datos para generar excel', 'danger')
        else:
            try:
                arr1 = filtro.excelFich(dat, 'ID_ficha', tab)
                #unicos = filtro.valores_unicos(arr1, 3)
                # creacion del excel
                excel = openpyxl.Workbook()
                sheet = excel.active
                sheet['A1'] = "Ficha:"
                sheet['B1'] = arr1[0][0]

                sheet['B3'] = "FICHA" 
                sheet['C3'] = "DOCENTE" 
                sheet['D3'] = "FECHA"
                sheet['E3'] = "DIA" 
                sheet['F3'] = "HORA" 

                for index, row in enumerate(arr1):
                    sheet[f'B{index+4}'] = row[0]                       
                    sheet[f'C{index+4}'] = row[5]+row[6]                       
                    sheet[f'D{index+4}'] = row[1]                       
                    sheet[f'E{index+4}'] = row[2]   
                    sheet[f'F{index+4}'] = str(row[3])+' am'+" - "+str(row[4])+' am'   
                excel.save("horario_1.xlsx")
                mensaje = "el excel se genero correctamente"
                flash(mensaje)
            except:
                print('hay un error con los datos para generar excel', 'danger')
                flash('hay un error con los datos para generar excel', 'danger')
                           
    return render_template('pages/descargas.html')