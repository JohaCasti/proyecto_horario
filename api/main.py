from flask import Flask, request
from modelsApi import Query
from werkzeug.security import generate_password_hash
import json
import datetime


def createapp():
    app = Flask(__name__)

    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'devBare',
        SERVER_API = "http://127.0.0.1:8000",
        PUERTOAPP = 8000
    )
    
    @app.route('/api')
    def index():
        return "hola mundo... del api"
    
    # COLSULTAS
    @app.route('/consult/<list>')
    def listar(list):
        sql="SELECT * FROM "+list
        #LIMIT 10;   pendiente para solo traer 10 registros a la vez!
        l = Query()
        x = l.EjecutarQuery(sql)
        return x
    # CONSULTA DATOS POR ID
    @app.route('/consult/datos/<id>/<col>/<tab>')
    def identi(id, col, tab):
        #a = f'SELECT * FROM admin WHERE  Tipo_admin ="{id}"'
        a = f'SELECT * FROM {tab} WHERE {col}="{id}"'
        sql= a
        f = Query()
        x = f.EjecutarUno(sql)
        print(x)
        return x
    @app.route('/consult/todos/<id>/<col>/<tab>')
    def todosI(id, col, tab):
        a = f'SELECT b.ID_bloque, b.HoraIni, b.HoraFin, b.Start, f.Ficha FROM {tab} as b LEFT join Fichas as f ON b.id_ficha=f.ID_ficha WHERE {col}={id}'
        sql= a
        print(sql)
        f = Query()
        x = f.EjecutarQuery(sql)
        return x
    @app.route('/consult/todas/<id>/<col>/<tab>')
    def todosF(id, col, tab):
        a = f'SELECT b.ID_bloque, b.HoraIni, b.HoraFin, b.Start, i.Nombre, i.Apellido FROM {tab} as b LEFT join Instructores as i ON b.id_instructor=i.ID_instructores WHERE {col}={id}'
        sql= a
        print(sql)
        f = Query()
        x = f.EjecutarQuery(sql)
        return x
    # CONSULTA Y TRAE SOLO EL ID PARA EXCEL
    @app.route('/consult/idexcel/<id>/<col>/<col1>/<tab>')
    def excel(id, col, tab, col1):
        #a = f'SELECT * FROM admin WHERE  Tipo_admin ="{id}"'
        a = f'SELECT ID_{col1} FROM {tab} WHERE {col}="{id}"'
        sql= a
        print(sql)
        f = Query()
        x = f.EjecutarUno(sql)
        print(x)
        return x
    # consulta con un like, variedad de datos con parecidos
    @app.route('/consult/espec/<dat>/<tab>/<colum>')
    def first(dat, tab, colum):
        a = f"SELECT * FROM {tab} where {colum} LIKE '%{dat}%' "
        sql= a
        f = Query()
        x = f.EjecutarUno(sql)
        return x, {'Access-Control-Allow-Origin':'*'}
    # trae datos de un id especifico del admin
    @app.route('/consult/especifid/<id>')
    def id(id):
        a = f'SELECT * FROM Admin where ID_admin="{id}"'
        sql= a
        f = Query()
        x = f.EjecutarUno(sql)
        #print(x)
        return x
    #traer la suma de los resultados
    @app.route('/api/all/<tab>')
    def suma(tab):
        a = f"SELECT COUNT(*) FROM {tab}"
        sql=a
        l = Query()
        x = l.EjecutarUno(sql)
        return x
    # CONSULTA RESTRICCION DE HORAS
    @app.route('/consult/restriccion/<id>/<tab>')
    def horasT(id, tab):
        if tab == "Instructores":
            i = f"SELECT HorasTotal FROM Instructores WHERE ID_instructores={id}"
            sql= i
            f = Query()
            x = f.consultApi(sql)
            return x
        elif tab == "Ambientes":
            i = f"SELECT HorasDia FROM Ambientes WHERE ID_ambiente={id}"
            sql= i
            f = Query()
            x = f.consultApi(sql)
            return x
        else:
            i = f"SELECT HorasTotal FROM Actividades WHERE ID_actividades={id}"
            sql= i
            f = Query()
            x = f.consultApi(sql)
            return x
    #CONSULTAS CON JOIN
    # JOIN SIMPLE TRAER TODOS LOS DATOS
    @app.route('/consult/jall/<tab1>/<tab2>/<dat1>/<dat2>')
    def joinE(tab1, tab2, dat1, dat2):
        a =f"SELECT * FROM {tab1} AS z LEFT JOIN {tab2} AS y  ON  z.{dat1}=y.{dat2}"
        sql = a
        l = Query()
        x = l.EjecutarQuery(sql)
        return x
    # JOIN SIMPLE CON UN WHERE
    @app.route('/consult/dos/<dat>/<dat1>/<dat2>/<dat3>/<dat4>/<dat5>/<dat6>/<dat7>')
    def joinD(dat1,dat, dat2, dat3, dat4, dat5, dat6, dat7):
        a = f'SELECT i.*, c.{dat}, c.{dat1} FROM {dat2} as i LEFT JOIN {dat3} as c ON i.{dat4}=c.{dat5} WHERE {dat6}={dat7}'
        sql = a
        print(sql)
        print('arriba esta el sql')
        l = Query()
        x = l.EjecutarUno(sql)
        return x
    # JOIN TRES TABLAS
    @app.route('/consult/tres/<dat>/<dat1>/<dat2>/<dat3>/<dat4>/<dat5>/<dat6>/<dat7>/<dat8>/<dat9>/<dat10>')
    def joinT(dat ,dat1, dat2, dat3, dat4, dat5, dat6, dat7, dat8, dat9, dat10):
        a = f'SELECT i.*,s.{dat8}, s.{dat}, c.{dat5}, c.{dat1} FROM {dat2} as i LEFT JOIN {dat3} as c ON i.{dat4}=c.{dat5} LEFT JOIN {dat6} as s ON c.{dat7}=s.{dat8} WHERE {dat9}={dat10}'
        sql = a
        print(sql)
        print('arriba esta el sql')
        l = Query()
        x = l.EjecutarUno(sql)
        return x
    # JOIN CUATRO TABLAS
    @app.route('/consult/cua/<dat>/<dat1>/<dat2>/<dat3>/<dat4>/<dat5>/<dat6>/<dat7>/<dat8>/<dat9>/<dat10>/<dat11>/<l>/<dat12>/<dat13>/<dat14>')
    def joinC(dat ,dat1, dat2, dat3, dat4, dat5, dat6, dat7, dat8, dat9, dat10, dat11, l, dat12, dat13, dat14):
        a = f'SELECT i.*, c.{dat}, c.{dat1},s.{dat2}, s.{dat3}, z.{dat4}, z.{dat5} FROM {dat6} as i LEFT JOIN {dat7} as c ON i.{dat8}=c.{dat} LEFT JOIN {dat9} as s ON c.{dat10}=s.{dat2} LEFT JOIN {dat11} as z ON {l}.{dat12}=z.{dat4} WHERE {dat13}={dat14}'
        sql = a
        print(sql)
        print('arriba esta el sql')
        l = Query()
        x = l.EjecutarUno(sql)
        return x
    # JOIN EN CASCADA
    @app.route('/consult/cascada/<tab>')
    def joinCas(tab):
        if tab == 'Ambientes':
            a = f'SELECT f.*, s.Sede, c.Centro FROM {tab} as f JOIN Sedes as s ON f.id_sede = s.ID_sedes JOIN Centros AS c ON s.id_centro = c.ID_centro'
            sql = a
            l = Query()
            x = l.EjecutarQuery(sql)
            return x
        else:   
            a =f"SELECT f.*, p.Programa, s.Sede, c.Centro FROM {tab} as f JOIN Programas as p ON f.id_Programa = p.ID_programa JOIN Sedes as s ON p.id_sede = s.ID_sedes JOIN Centros AS c ON s.id_centro = c.ID_centro"
            sql = a
            l = Query()
            x = l.EjecutarQuery(sql)
            return x
    
    # CONSULTAR DATOS API JAVASCRIPT
    @app.route('/api/conall/<dat1>/<dat2>/<tab>/<dat3>/<id>')
    def apiDatos(dat1, dat2, tab, dat3, id):
        a = f"SELECT {dat1}, {dat2} FROM {tab} WHERE {dat3}='{id}'"
        sql=a
        #LIMIT 10;   pendiente para solo traer 10 registros a la vez!
        l = Query()
        x = l.EjecutarQuery(sql)
        return x, {'Access-Control-Allow-Origin':'*'}
    # CONSULTAR DATOS PARA EXCEL
    @app.route('/api/excel/<tab>')
    def excelDatos(tab):
        a = f"SELECT * FROM {tab}"
        sql=a
        #LIMIT 10;   pendiente para solo traer 10 registros a la vez!
        l = Query()
        x = l.EjecutarQuery(sql)
        return x, {'Access-Control-Allow-Origin':'*'}
    
    # REGISTRAR COSAS
    # REGISTRAR ADMIN
    @app.route("/consult/regisadmin", methods=['POST'])
    def regisAdmin():
        data=request.get_json()
        print(data)
        nombre = data['nombre']
        apellido = str(data['apellido'])
        tipo_admin = str(data['tipo_admin'])
        username = str(data['username'])
        password = data['password']
        passwd = str(generate_password_hash(password))
        sql="INSERT INTO admin VALUES (null, '"+nombre+"','"+apellido+"','"+tipo_admin+"','"+username+"','"+passwd+"')"
        r = Query()
        result = r.Ejecutar(sql)
        print(sql)
        return result
    #INSERTAR CENTROS
    @app.route('/insertar/ce', methods=['POST'])
    def insertcent():
            data=request.get_json()
            tabla = data['lugar']
            nombre = data['nombre']
            telefono = data['telefono']
            descripcion = data['descripcion']

            peticion = f'INSERT INTO {tabla} VALUES (NULL, "{nombre}", "{telefono}", "{descripcion}")'
            sql = peticion
            r = Query()
            result = r.Ejecutar(sql)
            print(sql)
            return result
    #INSERTAR SEDES
    @app.route('/insertar/se', methods=['POST'])
    def insertsed():
        data=request.get_json()
        tabla = data['lugar']
        centro = data['id_centro']
        nombre = data['nombre']
        descripcion = data['descripcion']
        peticion = f'INSERT INTO {tabla} VALUES (NULL, {centro}, "{nombre}", "{descripcion}")'
        sql = peticion
        print(sql)
        r = Query()
        result = r.Ejecutar(sql)
        return result
    # INSERTAR AMBIENTES
    @app.route('/insertar/amb', methods=['POST'])
    def insertamb():
        data=request.get_json()
        tabla = data['lugar']
        sede = data['id_sede']
        nombre = data['nombre']
        horas = data['horas']
        descripcion = data['descripcion']
        peticion = f'INSERT INTO {tabla} VALUES (NULL, {sede}, {nombre}, {horas}, 0, "{descripcion}")'
        sql = peticion
        print(sql)
        r = Query()
        result = r.Ejecutar(sql)
        return result
    #INSERTAR PROGRAMAS
    @app.route('/insertar/pro', methods=['POST'])
    def insertpro():
        data=request.get_json()
        tabla = data['lugar']
        sede = data['id_sede']
        nombre = data['nombre']
        titulo = data['id_titulo']
        descripcion = data['descripcion']

        peticion = f'INSERT INTO {tabla} VALUES (NULL,"{sede}", "{nombre}", {titulo}, "{descripcion}")'
        sql = peticion
        r = Query()
        result = r.Ejecutar(sql)
        print(sql)
        return result
    #INSERTAR FICHAS
    @app.route('/insertar/fich', methods=['POST'])
    def insertfich():
        data=request.get_json()
        tabla = data['lugar']
        programa = data['id_programa']
        ficha = data['ficha']
        descripcion = data['descripcion']
        peticion = f'INSERT INTO {tabla} VALUES (NULL, {programa}, "{ficha}", "{descripcion}")'
        sql = peticion
        r = Query()
        result = r.Ejecutar(sql)
        print(sql)
        return result
    #INSERTAR ACTIVIDADES
    @app.route('/insertar/acti', methods=['POST'])
    def insertacti():
        data=request.get_json()
        tabla = data['lugar']
        programa = data['id_programa']
        actividad = data['nombre']
        horas = data['horas']
        descripcion = data['descripcion']
        peticion = f'INSERT INTO {tabla} VALUES (NULL, {programa}, "{actividad}", {horas}, 0, "{descripcion}")'
        sql = peticion
        print(sql)
        r = Query()
        result = r.Ejecutar(sql)
        return result
    #INSERTAR PROFESORES
    @app.route('/insertar/inst', methods=['POST'])
    def insertinst():
        data=request.get_json()
        tabla = data['lugar']
        centro = data['id_centro']
        nombre = data['nombre']
        apellidos = data['apellido']
        identi = data['identi']
        email = data['correo']
        contra = data['contra']
        horas = data['horas']
        paswd = data['paswd']
        passwd =str(generate_password_hash(paswd))
        peticion = f'INSERT INTO {tabla} VALUES (NULL, {centro}, "{nombre}", "{apellidos}", "{identi}", "{email}", "{contra}", {horas}, 0, "{passwd}")'
        sql = peticion
        print(sql)
        r = Query()
        result = r.Ejecutar(sql)
        return result
    # CREACION DE HORAS DOCENTES, SALONES Y ACTIVIDADES
    # CONSULTA INSTRUCTORES
    # @app.route('/in/horasdocente', methods=['POST'])
    def horasdocente(id, dato):
        a = f"SELECT * FROM HorasInstru WHERE id_instructor='{id}' AND Semana='{dato}'"
        sql= a
        f = Query()
        x = f.consultApi(sql)
        print(x)
        return x
    # CONSULTA SALONES 
    def horasSalon(id, dato):
        a = f"SELECT * FROM HorasAmbi WHERE id_ambiente='{id}' AND Dia='{dato}'"
        sql= a
        f = Query()
        x = f.consultApi(sql)
        return x
    # CONSULTA ACTIVIDADES
    def horasActividad(id, ficha):
        a = f"SELECT * FROM HorasActi WHERE id_actividad='{id}' AND id_ficha='{ficha}'"
        sql= a
        f = Query()
        x = f.consultApi(sql)
        return x
    
    # COMPROBASION  DE HORAS DOCENTE, SALON Y ACTIVIDAD
    def comprobacion(horas_totales, id_docente, id_salon, id_actividad, semana, dia, ficha, horas, dias_sem):
        # consultas
        consultI = horasdocente(id_docente, semana)
        consultS = horasSalon(id_salon, dia)
        consultA = horasActividad(id_actividad, ficha)
        consHoraI = horasT(id_docente, "Instructores")
        consHoraS = horasT(id_salon, "Ambientes")
        consHoraA = horasT(id_actividad, "Actividades")
        print("seguimiento")
        print(consHoraI)
        print(consultI)
        print(consHoraS)
        print(consultS)
        print(consHoraA)
        print(consultA)
        # restriccion docentes
        if consultI == None:
            consHoraI = int(consHoraI[0])
            consultI = 0
            z = horas * dias_sem
            if (consultI + z) > consHoraI:
                suma = consultI + horas_totales
                print(suma)
                mensaje = "1El horario no se puede crear porque el docente pasa sus horas de trabajo semanal"
                print(mensaje)
                return mensaje
        else:
            hor = int(consultI[3])
            consHoraI = int(consHoraI[0])
            z = horas * dias_sem
            if (hor + z) > consHoraI:
                mensaje = "El horario no se puede crear porque el docente pasa sus horas de trabajo semanal"
                print(mensaje)
                return mensaje
        # restriccion salones
        if consultS == None:
            consHoraS = int(consHoraS[0])
            consultS = 0
            if (consultS + horas) > consHoraS:
                mensaje = "1El horario no se puede crear porque el salon ya sobrepaso sus horas diarias"
                print(mensaje)
                return mensaje
        else:
            hor = int(consultS[3])
            consHoraS = int(consHoraS[0])
            if (hor + horas) > consHoraS:
                mensaje = "El horario no se puede crear porque el salon ya sobrepaso sus horas diarias"
                print(mensaje)
                return mensaje
        # restriccion actividades
        if consultA == None:
            consHoraA = int(consHoraA[0])
            consultA = 0
            if (consultA + horas) > consHoraA:
                mensaje = "1El horario no se puede crear porque la actividad ya sobrepaso sus horas"
                print(mensaje)
                return mensaje
        else:
            hor = int(consultA[3])
            consHoraA = int(consHoraA[0])
            if (hor + horas) > consHoraA:
                mensaje = "El horario no se puede crear porque la actividad ya sobrepaso sus horas"
                print(mensaje)
                return mensaje
        print("aqui vamos")
        # docente
        if consultI == None or consultI == 0:
            a = f'INSERT INTO HorasInstru VALUES (NULL, "{id_docente}", "{semana}", "{horas}")'
            sql = a
            print(sql)
            r = Query()
            result = r.Ejecutar(sql)
        else:
            hi = int(consultI[3])
            hTotal = hi + horas
            print("else:")
            print(consHoraI)
            restri = int(consHoraI)
            if hTotal < restri:
                queri = f"UPDATE HorasInstru SET Horas='{hTotal}' WHERE id_instructor='{id_docente}' AND Semana='{semana}'"
                sql = queri
                print(sql)
                f = Query()
                x = f.Ejecutar(sql)
                print(x)
        # salon
        if consultS == None or consultS == 0:
            a = f'INSERT INTO HorasAmbi VALUES (NULL, "{id_salon}", "{dia}", "{horas}")'
            sql = a
            print(sql)
            r = Query()
            result = r.Ejecutar(sql)
        else:
            hs = int(consultS[3])
            hTotal1 = hs + horas
            restri1 = int(consHoraS)
            if hTotal1 < restri1:
                query = f"UPDATE HorasAmbi SET Horas='{hTotal1}' WHERE id_ambiente='{id_salon}' AND Dia='{dia}'"
                sql = query
                print(sql)
                f = Query()
                x = f.Ejecutar(sql)
                print(x)
        # actividad
        if consultA == None or consultA == 0:
                a = f'INSERT INTO HorasActi VALUES (NULL, "{id_actividad}", "{ficha}", "{horas}")'
                sql = a
                print(sql)
                r = Query()
                result = r.Ejecutar(sql)
        else:
            ha = int(consultA[3])
            hTotal2 = ha + horas
            restri2 = int(consHoraA)
            if hTotal2 < restri2:
                queri = f"UPDATE HorasActi SET Horas='{hTotal2}' WHERE id_actividad='{id_actividad}' AND id_ficha='{ficha}'"
                sql = queri
                print(sql)
                f = Query()
                x = f.Ejecutar(sql)
                print(x)
    

    # CREAR HORARIO
    # SEPARAR LOS HORARIOS
    @app.route('/separent/crear/horacal', methods=['POST'])   
    def separacion():
        data=request.get_json()
        start = data['start']
        end = data['end']
        hora_ini= data['hora_i']
        hora_fin = data['hora_f']
        centro = data['centro']
        sede = data['sede']
        instructor = data['instructor']
        salon = data['salon']
        programa = data['programa']
        ficha = data['ficha']
        acti = data['acti']
        datos = data['datos']
        horas = data['horas']
        dias = data['dias']
        horas_totales = data['horas_totales']

        print(start)
        print(end)
        print(hora_ini)
        print(hora_fin)
        print(horas)
        print("api")
        print(dias)
        dias_sem = len(dias)        
         # division por dias y semanas
        class Horario:
            def __init__(self, fecha_inicio, fecha_fin):
                self.fecha_inicio = datetime.date.fromisoformat(fecha_inicio)
                self.fecha_fin = datetime.date.fromisoformat(fecha_fin)

            def calcular_dias(self):
                return (self.fecha_fin - self.fecha_inicio).days

            def generar_fechas(self, incluir_domingos=False, dias_seleccionados=None):
                if dias_seleccionados is None:
                    dias_seleccionados = list(range(6))  # Por defecto incluye todos los días (0 a 5) MENOS DOMINGO

                fechas = []
                semanas = []
                for i in range(self.calcular_dias() + 1):
                    fecha = self.fecha_inicio + datetime.timedelta(days=i)
                    if (incluir_domingos or fecha.weekday() != 6) and fecha.weekday() in dias_seleccionados:
                        semana = fecha.isocalendar()[1]  # Obtiene el número de la semana
                        fechas.append(fecha.strftime('%Y-%m-%d'))
                        semanas.append(semana)

                return list(zip(fechas, semanas))
    
        crear = Horario(start, end)
        fechas_con_semanas = crear.generar_fechas(incluir_domingos=True, dias_seleccionados=dias)  # lunes = 0 y domingo = 6
        for fecha, semana in fechas_con_semanas:
            print(f"{fecha} (Semana {semana})")
            #d = horasdocente(instructor, semana, horas)
            #s = horasSalon(salon, fecha, horas)
            #m = horasActividad(acti, ficha, horas)
            totalHor = comprobacion(horas_totales, instructor, salon, acti, semana, fecha, ficha, horas, dias_sem)
            print("resultado final:")
            if totalHor == None:
                print("se guardo correctamente")
                peticion = f'INSERT INTO Bloques VALUES (NULL, "{centro}", "{sede}", "{salon}", "{instructor}", "{programa}", "{ficha}", "{acti}", "{hora_ini}", "{hora_fin}", "{fecha}", "{fecha}", "{datos}")'
                sql = peticion
                r = Query()
                result = r.Ejecutar(sql)
            else:
                print(totalHor)
                return totalHor
                
    # ACTULIZAR TABLAS
    # ACTUALIZAR 1
    @app.route('/update/t/<tab>/<nom>/<tel>/<des>/<id>/<nom1>/<tel1>/<des1>/<id1>', methods=['PUT','POST'])
    def updateT(tab, nom, tel, des, id, nom1, tel1, des1, id1):
        a = f"UPDATE {tab} SET {nom}='{nom1}', {tel}='{tel1}', {des}='{des1}' WHERE {id}='{id1}'"
        sql = a
        print(sql)
        f = Query()
        x = f.Ejecutar(sql)
        print(x)
        return x
    # ACTUALIZAR INSTRUCTOR
    @app.route('/update/in/<cen>/<nom>/<ape>/<iden>/<mail>/<con>/<hor>/<id>', methods=['PUT','POST'])
    def updatein(cen, nom, ape, iden, mail, con, hor, id):
        a = f"UPDATE Instructores SET id_centro={cen}, Nombre='{nom}', Apellido='{ape}', NumIdenti='{iden}', Correo='{mail}', Tipocontrato='{con}', HorasTotal={hor} WHERE ID_Instructores={id}"
        sql = a
        print(sql)
        f = Query()
        x = f.Ejecutar(sql)
        print(x)
        return x
    # ACTUALIZAR 2
    @app.route('/update/act/<a>/<dat>/<dat1>/<dat2>/<dat3>/<dat4>/<dat5>/<dat6>/<dat7>/<dat8>/<dat9>', methods=['PUT','POST'])
    def updateact(a, dat, dat1, dat2, dat3, dat4, dat5, dat6, dat7, dat8, dat9):
        a = f"UPDATE {a} SET {dat}='{dat1}', {dat2}='{dat3}', {dat4}='{dat5}', {dat6}='{dat7}' WHERE {dat8}='{dat9}'"
        sql = a
        print(sql)
        f = Query()
        x = f.Ejecutar(sql)
        print(x)
        return x
    # ACTUALIZAR ACTIVIDADES
    @app.route('/update/acti/<a>/<dat>/<dat1>/<dat2>/<id>', methods=['PUT','POST'])
    def updateacti(a, dat, dat1, dat2, id):
        a = f"UPDATE Actividades SET id_programa={a}, Actividad='{dat}', HorasTotal={dat1}, Descripcion='{dat2}' WHERE ID_actividades={id}"
        sql = a
        print(sql)
        f = Query()
        x = f.Ejecutar(sql)
        print(x)
        return x
    # ACTUALIZAR SEDES
    @app.route('/update/sed/<dat>/<dat1>/<dat2>/<id>', methods=['PUT','POST'])
    def updatesed(dat, dat1, dat2, id):
        a = f"UPDATE Sedes SET id_centro={dat}, Sede='{dat1}', Descripcion='{dat2}' WHERE ID_sedes={id}"
        sql = a
        print(sql)
        f = Query()
        x = f.Ejecutar(sql)
        print(x)
        return x
    # ACTUALIZAR AMBIENTE
    @app.route('/update/ambi/<dat>/<dat1>/<dat2>/<dat3>/<id>', methods=['PUT','POST'])
    def updateambi(dat, dat1,dat2,dat3,id):
        a = f"UPDATE Ambientes SET id_sede='{dat}', Ambiente='{dat1}', HorasDia='{dat2}', Descripcion='{dat3}' WHERE ID_ambiente='{id}'"
        sql = a
        print(sql)
        f = Query()
        x = f.Ejecutar(sql)
        print(x)
        return x
    # ACTUALIZAR PROGRAMA
    @app.route('/update/pro/<dat>/<dat1>/<dat2>/<dat3>/<id>' , methods=['PUT','POST'])
    def updatepro(dat, dat1, dat2, dat3, id):
        a = f"UPDATE Programas SET id_sede='{dat}', Programa='{dat1}', id_titulacion={dat2}, Descripcion='{dat3}' WHERE ID_programa={id}"
        sql = a
        print(sql)
        f = Query()
        x = f.Ejecutar(sql)
        print(x)
        return x
    #  ACTUALIZAR  FICHAS
    @app.route('/update/ficha/<data>/<data1>/<data2>/<data3>' , methods=['PUT', 'POST'])
    def updateficha(data, data1, data2, data3):
        a = f"UPDATE Fichas SET id_programa='{data}', Ficha='{data1}', Descripcion='{data2}' WHERE ID_ficha={data3}"
        sql = a
        print(sql)
        f = Query()
        x = f.Ejecutar(sql)
        print(x)
        return x 
    # ACTUALIZAR PERFIL ADMIN
    @app.route('/update/perf/<id>/<dat>/<dat1>/<dat2>/<dat3>', methods=['PUT', 'POST'])
    def updateperf(id, dat, dat1, dat2, dat3):
        a = f"UPDATE Admin SET Nombre='{dat}', Apellido='{dat1}', Identificacion='{dat2}', Correo='{dat3}' WHERE ID_admin='{id}'"
        sql = a
        print(sql)
        f = Query()
        x = f.Ejecutar(sql)
        print(x)
        return x
    return app
if __name__ == '__main__':
    app = createapp()
    app.run(port=8000)