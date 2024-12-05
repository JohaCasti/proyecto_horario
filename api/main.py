from flask import Flask, request
from modelsApi import Query
from werkzeug.security import generate_password_hash
import json
import datetime
from datetime import datetime, timedelta, date


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
    @app.route('/api/datostab/<div>/<sed>/<ambi>')
    def datosTabla(sed, ambi, div):
        a = f"SELECT B.ID_bloque, C.Centro AS Centro, S.Sede AS Sede, A.Ambiente AS Ambiente, I.Nombre AS Instructor, I.Apellido AS Instructor, P.Programa AS Programa, F.Ficha AS Ficha, AC.Actividad AS Actividad, B.Horabloq AS Horario, B.Fecha, B.id_div FROM  Bloques B JOIN  Centros C ON B.id_centro = C.ID_centro JOIN Sedes S ON B.id_sede = S.ID_sedes JOIN Ambientes A ON B.id_ambiente = A.ID_ambiente JOIN Instructores I ON B.id_instructor = I.ID_instructores JOIN Programas P ON B.id_programa = P.ID_programa JOIN Fichas F ON B.id_ficha = F.ID_ficha JOIN Actividades AC ON B.id_actividad = AC.ID_actividades WHERE B.id_div ={div} AND B.id_sede={sed} AND B.id_ambiente={ambi};"
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
    
    def horasActi(id):
        a = f"SELECT ID_actividades, HorasTotal FROM Actividades WHERE ID_actividades='{id}'"
        sql= a
        f = Query()
        x = f.EjecutarUno(sql)
        return x , {'Access-Control-Allow-Origin':'*'}
    # SABER LAS HORAS DE TRABAJO INSTRUCTOR
    @app.route('/calc/<id>')
    def calcHoras(id):
        print("aqui vamos en el api calcular horas del docente")
        a = f"SELECT hi.id_instructor, hi.Horas, i.HorasTotal FROM HorasInstru AS hi LEFT JOIN Instructores AS i ON hi.id_instructor=i.ID_instructores WHERE hi.id_instructor='{id}'"
        sql=a
        l = Query()
        x = l.EjecutarUno(sql)
        print(x)
        return x, {'Access-Control-Allow-Origin':'*'}
    @app.route('/calma/<id>')
    def calmaAc(id):
        print("aqui vamos en el api calcular horas de la actividad")
        a = f"SELECT ha.id_actividad, ha.Horas, i.HorasTotal FROM HorasActi AS ha LEFT JOIN Actividades AS i ON ha.id_actividad=i.ID_actividades WHERE ha.id_actividad='{id}'"
        sql=a
        l = Query()
        x = l.EjecutarUno(sql)
        print(x)
        return x, {'Access-Control-Allow-Origin':'*'}
    # COMPROBASION  DE HORAS DOCENTE, SALON Y ACTIVIDAD
    @app.route('/comp/<ambi>/<id>/<ins>/<sede>/<fi>/<ma>/<hora>/<dia>')
    def comprobacion(ambi, id, ins, sede, fi, ma, hora, dia):
        print("aqui vamos en el api comprobacion")
        # consultas
        # CONSULTA DE SALON Y FEHCA Y HORA
        a = f"SELECT * FROM Bloques WHERE id_ambiente={ambi} AND id_div={id}" 
        sql= a
        f = Query()
        x = f.EjecutarUno(sql)
        print(x)
        print("seguimiento")
        # CONSULTA DE DOCENTE Y HORA
        b = f"SELECT * FROM Bloques WHERE id_instructor={ins} AND Horabloq='{hora}' AND Fecha='{dia}'" 
        sql= b
        g = Query()
        y = g.EjecutarUno(sql)
        ylist = json.loads(y)
        print(ylist)    
        print("seguimiento y")
        # CONSULTA DE FICHA Y HORA
        c = f"SELECT * FROM Bloques WHERE id_ficha={fi} AND Horabloq='{hora}' AND Fecha='{dia}'" 
        sql= c
        h = Query()
        z = h.EjecutarUno(sql)
        zli = json.loads(z)
        print(zli)    
        print("seguimiento z")

        if ylist not in [None, 'null']:
            print("entramos a y:")
            mensaje = [f"EL instructor ya esta ocupado a esa hora y dia, en la sede:{ylist[2]} y salon:{ylist[3]}"]
            return mensaje
        if zli not in [None, 'null']:
            print("entramos a z:")
            mensaje = ["La ficha ya esta ocupado a esa hora y dia"]
            return mensaje
        if x is None or x == 'null':
            return 'null'
        else:
            datins = x[5]
            datambi = x[4]
            datsede = x[2]
            datfi = x[6]
            datma = x[7]
            dathor = x[8]
            datdia = x[9]
            if datsede != sede:
                if datins == ins:
                    pass

            mensaje = "hay una coincidencia"
            return x        
    # CREAR HORARIO
    # SEPARAR LOS HORARIOS
    @app.route('/confi/crear/horacal', methods=['POST'])   
    def confirmacionBlo():
        data=request.get_json()
        centro = data['centro']
        sede = data['sede']
        instructor = data['instructor']
        salon = data['salon']
        programa = data['programa']
        ficha = data['ficha']
        acti = data['acti']
        horas = data['horas']
        dias = data['dias']
        id = data['id']

        peticion = f'INSERT INTO Bloques VALUES (NULL, "{centro}", "{sede}", "{salon}", "{instructor}", "{programa}", "{ficha}", "{acti}", "{horas}", "{dias}", "{id}")'
        sql = peticion
        r = Query()
        result = r.Ejecutar(sql)
        print(result)
        print("info de guardado")
        return result
    # GUARDAR HORAS DOCENTE Y ACTIVIDAD
    @app.route('/agre/dual/<id>/<hor>/<acti>/<fi>', methods=['POST', 'PUT'])
    def horasDual(id, hor, acti, fi):
        #  consultar si ya existe o toca crearla
        datosInstru = identi(id, "id_instructor", "HorasInstru")
        datosActi = identi(acti, "id_actividad", "HorasActi")
        print("guardando datos de horas:")
        print(datosInstru)
        if datosInstru == "null" or datosInstru == None:
            # horas instructor
            peti1 = f'INSERT INTO HorasInstru VALUES (NULL, "{id}", 12, "{hor}")'
            consult1 = peti1
            r = Query()
            result1 = r.Ejecutar(consult1)
            print(result1)
            print("info de guardada, en Horas Instructor")
        else:
            horasI = datosInstru[3] + 1
            a = f"UPDATE HorasInstru SET Horas='1' WHERE id_instructor='{id}'"
            sql = a
            print(sql)
            f = Query()
            x = f.Ejecutar(sql)
            print(x)

        if datosActi == "null" or datosActi == None:
            # horas actividad 3mestral
            peti2 = f'INSERT INTO HorasActi VALUES (NULL, "{acti}", "{fi}", "{hor}")'
            consult2 = peti2
            o = Query()
            result2 = o.Ejecutar(consult2)
            print(result2)
            print("info de guardada, en Horas activida")
        else:
            horasA = datosActi[3] + 1
            a = f"UPDATE HorasActi SET Horas='1' WHERE id_actividad='{acti}' AND id_ficha='{fi}'"
            sql = a
            print(sql)
            f = Query()
            x = f.Ejecutar(sql)
            print(x)
        
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