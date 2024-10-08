from flask import Flask, request
from models import Query
from werkzeug.security import generate_password_hash, check_password_hash

def createapp():
    app = Flask(__name__)

    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'devBare',
    )

    @app.route('/api')
    def index():
        return "hola mundo... del api"
    

    # CONSULTAR DATOS API JAVASCRIPT
    #http://127.0.0.1:8000/api/consult/id
    @app.route('/api/conall/<dat1>/<dat2>/<tab>/<dat3>/<id>')
    def programasCentro(dat1, dat2, tab, dat3, id):
        a = f"SELECT {dat1}, {dat2} FROM {tab} WHERE {dat3}='{id}'"
        sql=a
        #LIMIT 10;   pendiente para solo traer 10 registros a la vez!
        l = Query()
        x = l.EjecutarQuery(sql)
        return x, {'Access-Control-Allow-Origin':'*'}


    @app.route('/api/all/<tab>')
    def suma(tab):
        a = f"SELECT COUNT(*) FROM {tab}"
        sql=a
        l = Query()
        x = l.EjecutarUno(sql)
        return x

    # SUMAR RESULTADOS DE ALGO ESPECIFICO Y TRAER EL TOTAL
    @app.route('/api/sumreg/<ta>/<dat>/<id>')
    def sumaregis(ta, dat, id):
        a = f"SELECT COUNT(*) FROM {ta} WHERE {dat}='{id}'"
        sql=a
        l = Query()
        x = l.EjecutarQuery(sql)
        return x, {'Access-Control-Allow-Origin':'*'}
    
    #http://127.0.0.1:8000/
    #consult/  ... api de consulta
    #update/ .... api actualizacion
    # mostrar todo de una tabla especifica
    @app.route('/consult/<list>')
    def listar(list):
        sql="SELECT * FROM "+list
        #LIMIT 10;   pendiente para solo traer 10 registros a la vez!
        l = Query()
        x = l.EjecutarQuery(sql)
        return x
    
    # consulta con join
    #SELECT *
    #FROM programas AS p
    #LEFT JOIN centro AS c ON p.centro=c.id_centro
    @app.route('/consult/left/<tab1>/<tab2>/<dat1>/<dat2>')
    def joinleft(tab1, tab2, dat1, dat2):
        a =f"SELECT * FROM {tab1} AS z LEFT JOIN {tab2} AS y  ON  z.{dat1}=y.{dat2}"
        sql = a
        l = Query()
        x = l.EjecutarQuery(sql)
        return x
    # join con where simple
    @app.route('/consult/joinespecif/<con>/<tab1>/<tab2>/<dat1>/<dat2>/<dat3>/<dat4>')
    def joinEspe(con, tab1, tab2, dat1, dat2, dat3, dat4):
        a =f"SELECT y.{con} FROM {tab1} AS z LEFT JOIN {tab2} AS y  ON  z.{dat1}=y.{dat2} WHERE {dat4}='{dat3}'"
        sql = a
        l = Query()
        x = l.EjecutarUno(sql)
        return x
    # JOIN CON WHERE COMPUESTO PARA CONDICIONAL, trae todos los datos de las tablas a comparar
    #SELECT *
    #FROM ficha AS f
    #LEFT JOIN Programas AS p, instructor AS i ON f.programa=p.id_programa
    #AND f.instructor=i.id_instructor
    @app.route('/consult/joinalltwo/<tab1>/<tab2>/<tab3>/<dat1>/<dat2>/<dat3>/<dat4>/')
    def joinAndall(tab1, tab2, tab3, dat1, dat2, dat3, dat4):
        a =f"SELECT * FROM {tab1} AS f LEFT JOIN {tab2} AS p, {tab3} AS i ON f.{dat1}=p.{dat2} AND f.{dat3}=i.{dat4}"
        sql = a
        l = Query()
        x = l.EjecutarQuery(sql)
        return x


    #traer todas los resultados de una columna en especifico de una tabla especifica
    @app.route('/consult/colum/<col>/<tab>')
    def columnas(col, tab):
        a = f"SELECT {col} FROM {tab}"
        sql= a
        l = Query()
        x = l.EjecutarQuery(sql)
        return x

    # traer toda informacion de algo especifico de una tabla especifica
    @app.route('/consult/espec/<dat>/<tab>/<colum>')
    def first(dat, tab, colum):
        a = f"SELECT * FROM {tab} where {colum} LIKE '%{dat}%' "
        sql= a
        f = Query()
        x = f.EjecutarUno(sql)
        return x
    
    # consultar una conincidencia con dos datos 
    @app.route('/consult/group/<tab>/<col1>/<da1>/<col2>/<da2>')
    def group(tab, col1, da1, col2, da2):
        a = f"SELECT * FROM {tab} where {col1}='{da1}' AND {col2}='{da2}'"
        sql= a
        print(sql)
        f = Query()
        x = f.EjecutarUno(sql)
        return x
    

    # consultar por id
    @app.route('/consult/datos/<id>/<col>/<tab>')
    def identi(id, col, tab):
        #a = f'SELECT * FROM admin WHERE  Tipo_admin ="{id}"'
        a = f'SELECT * FROM {tab} WHERE {col}="{id}"'
        sql= a
        f = Query()
        x = f.EjecutarUno(sql)
        print(x)
        return x
    
    
    @app.route('/consult/especifid/<id>')
    def id(id):
        a = f'SELECT * FROM admin where id_admin="{id}"'
        sql= a
        f = Query()
        x = f.EjecutarUno(sql)
        #print(x)
        return x


    # ACTUALIZAR DATOS
    #Actualizar un solo dato
    @app.route('/update/<tab>/<col>/<dat>/<col2>/<dat2>')
    def actualizar(tab, col, dat,col2, dat2):
        a = f"UPDATE {tab} SET {col} ='{dat}' WHERE {col2}='{dat2}'"
        sql= a
        f = Query()
        x = f.EjecutarUno(sql)
        return x
    
    #Actualizar todos los datos de centro
    @app.route('/update/centroall/<tab>/<nom>/<tel>/<des>/<id>', methods=['PUT','POST'])
    def actuacenall(tab, nom, tel, des, id):
        a = f"UPDATE {tab} SET Nombre='{nom}', Telefono='{tel}', Descrip='{des}' WHERE id_centro='{id}' "
        sql = a
        f = Query()
        x = f.Ejecutar(sql)
        print(x)
        return x
    
    # Actualizar todos los datos del programa
    @app.route('/update/programall/<tab>/<nom>/<tel>/<des>/<id>', methods=['PUT','POST'])
    def actuaproall(tab, nom, tel, des, id):
        a = f"UPDATE {tab} SET Nombre='{nom}', descripcion='{tel}', centro='{des}' WHERE id_programa='{id}' "
        sql = a
        f = Query()
        x = f.Ejecutar(sql)
        print(x)
        return x
    

    #ELIMINAR DATOS
    #Eliminar UN REGISTRO
    @app.route('/const/delete/<tab>/<col>/<dat>', methods=['DELETE','GET'])
    def borrar(tab, col, dat):
         a = f"DELETE FROM {tab} WHERE {col} ='{dat}'"
         sql = a
         print(sql)
         f = Query()
         x = f.Ejecutar(sql)


    
    # CREAR Y REGISTRAR
    @app.route("/consult/regisadmin", methods=['POST'])
    def regisAdmin():
        data=request.get_json() 
        print(data)
        nombre = data['nombre']
        apellido = str(data['apellido'])
        telefono = str(data['telefono'])
        tipo_admin = str(data['tipo_admin'])
        username = str(data['username'])
        password = data['password']
        passwd = str(generate_password_hash(password))
        sql="INSERT INTO admin(Nombre, Apellido, Telefono, Tipo_admin, Username, Password) VALUES ('"+nombre+"','"+apellido+"','"+telefono+"','"+tipo_admin+"','"+username+"','"+passwd+"')"
        r = Query()
        result = r.Ejecutar(sql)
        print(sql)
        return result
    

    
    @app.route('/consult/insertar/ce', methods=['POST'])
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
    
    @app.route('/consult/insertar/pro', methods=['POST'])
    def insertpro():
            data=request.get_json() 
            tabla = data['lugar']
            Nombre = data['Nombre']
            descripcion = data['descri']
            centro = data['centro']
        
            peticion = f'INSERT INTO {tabla} VALUES (NULL, "{Nombre}", "{descripcion}", "{centro}")'
            sql = peticion
            r = Query()
            result = r.Ejecutar(sql)
            print(sql)
            return result
        

    @app.route('/consult/insertar/sa', methods=['POST'])
    def insertsalo():
            data=request.get_json() 
            tabla = data['lugar']
            centro = data['centro']
            numero = data['numero']
            descripcion = data['descripcion']
        
            peticion = f'INSERT INTO {tabla} VALUES (NULL, "{centro}", "{numero}", "{descripcion}")'
            sql = peticion
            r = Query()
            result = r.Ejecutar(sql)
            print(sql)
            return result
    
    @app.route('/consult/insertar/fi', methods=['POST'])
    def insertficha():
            data=request.get_json() 
            tabla = data['lugar']
            ficha = data['ficha']
            programa = data['programa']
            instructor = data['instructor']
            descripcion = data['descripcion']
        
            peticion = f'INSERT INTO {tabla} VALUES (NULL, "{ficha}", "{programa}", "{instructor}", "{descripcion}")'
            sql = peticion
            r = Query()
            result = r.Ejecutar(sql)
            print(sql)
            return result
    

    @app.route('/consult/ingre/hor', methods=['POST'])
    def horarios():
         data=request.get_json() 
         start = data['start']
         end = data['end']
         centro = data['centro']
         instructor = data['instructor']
         salon = data['salon']
         ficha = data['ficha']
         color = data['color']
         datos = data['datos']

         peticion = f'INSERT INTO Horarios VALUES (NULL, "{start}", "{end}", "{centro}", "{instructor}", "{salon}","{ficha}""{color}", "{datos}")'
         sql = peticion
         r = Query()
         result = r.Ejecutar(sql)
         print(sql)
         return result
        


    # consultar los horarios creados
    @app.route('/consult/cruce/<dat1>/<dat2>/<dat3>/<dat4>/<dat5>/<dat6>/<dat7>/<dat8>')
    def cruce(dat1, dat2, dat3, dat4,dat5, dat6, dat7, dat8):
        a = f"SELECT * FROM Horarios WHERE (Centro_id='{dat1}' AND Salon_id='{dat3}') AND (Inicio<='{dat5}' AND Fin>='{dat7}') AND (Hora_ini<='{dat6}' AND Hora_fin>='{dat8}') AND (Instruc_id='{dat2}') AND (Ficha_id='{dat4}')"
        sql= a
        print(sql)
        f = Query()
        x = f.EjecutarUno(sql)
        if x == 'null':
            print(x)
            return x
        else:
            a = f"SELECT * FROM Horarios WHERE (Instruc_id={dat2}) AND (Inicio<='{dat5}' AND Fin>='{dat7}') AND (Hora_ini<='{dat6}' AND Hora_fin>='{dat8}')"
            sql= a
            print(sql)
            print('aqui llegue')
            f = Query()
            x = f.EjecutarUno(sql)
            if x == 'null':
                a = f"SELECT * FROM Horarios WHERE (Salon_id='{dat3}' AND Centro_id='{dat1}') AND (Inicio<='{dat5}' AND Fin>='{dat7}') AND (Hora_ini<='{dat6}' AND Hora_fin>='{dat8}')"
                sql= a
                print(sql)
                f = Query()
                x = f.EjecutarUno(sql)
                if x == 'null':
                    a = f"SELECT * FROM Horarios WHERE (Ficha_id='{dat4}') AND (Inicio<='{dat5}' AND Fin>='{dat7}') AND (Hora_ini<='{dat6}' AND Hora_fin>='{dat8}')"
                    sql= a
                    print(sql)
                    f = Query()
                    x = f.EjecutarUno(sql)
                    if x == 'null':
                        centro_search = f"SELECT nombre, id_horario FROM centro INNER JOIN Horarios ON id_centro = Centro_id WHERE (Centro_id='1' AND Salon_id='6') AND (Inicio<='06-08-2024' AND Fin>='08-08-2024') AND (Hora_ini<='11:00:00' AND Hora_fin>='15:00:00') AND (Instruc_id='2') AND (Ficha_id='4')"
                        sql= centro_search
                        f = Query()
                        x = f.EjecutarUno(sql)
                        if dat1 != x:
                            x = f"El instructor se encuentra en otro centro de formacion en esa fecha y horario"
                            return x
                    else:
                        x = f" El ficha {dat4} ya esta asignado en esa fecha y en ese horario"
                        return x
                else:
                    x = f" El salon {dat3} del {dat1} ya esta asignado en esa fecha y en ese horario"
                    return x
            else:
                x = f" El instructor ya esta asignado en esa fecha y en ese horario"
                return x



            #SELECT * FROM Horarios WHERE Inicio>'01-07-2024' AND Fin>='03-08-2024'

            # se cruzan fecha y hora 
            #SELECT * FROM Horarios WHERE (Centro_id='1' AND Salon_id='1') AND (Inicio<='06-08-2024' AND Fin>='06-08-2024') AND (Hora_ini<='11:00:00' AND Hora_fin>='11:00:00') AND (Instruc_id='2') AND (Ficha_id='1')

        return x




    return app

if __name__ == '__main__':
    app = createapp()
    app.run(port=8000)