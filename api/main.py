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
    
    #http://127.0.0.1:8000/consult/  ... api de consulta
    # mostrar todo de una tabla especifica
    @app.route('/consult/<list>')
    def listar(list):
        sql="SELECT * FROM "+list
        l = Query()
        x = l.EjecutarQuery(sql)
        return x

    # consultar algo especifico de una tabla especifica
    @app.route('/consult/espec/<dat>/<tab>/<colum>')
    def first(dat, tab, colum):
        a = f"SELECT * FROM {tab} where {colum} LIKE '%{dat}%' "
        sql= a
        f = Query()
        x = f.EjecutarUno(sql)
        return x
    
    @app.route('/consult/group/<tab>/<col1>/<da1>/<col2>/<da2>')
    def group(tab, col1, da1, col2, da2):
        a = f"SELECT * FROM {tab} where {col1}='{da1}' AND {col2}='{da2}'"
        sql= a
        print(sql)
        f = Query()
        x = f.EjecutarUno(sql)
        return x

    # consultar por id
    @app.route('/consult/especif/<id>')
    def identi(id):
        a = f'SELECT * FROM admin WHERE  Tipo_admin ="{id}"'
        sql= a
        f = Query()
        x = f.EjecutarQuery(sql)
        print(x)
        return x
    
    @app.route('/consult/especifid/<id>')
    def id(id):
        a = f'SELECT * FROM admin where id_admin="{id}"'
        sql= a
        f = Query()
        x = f.EjecutarUno(sql)
        print(x)
        return x

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
    
    @app.route('/consult/insertar/pr', methods=['POST'])
    def insertpro():
            data=request.get_json() 
            tabla = data['lugar']
            nombre = data['nombre']
            apellido = data['apellidos']
            identificacion = data['identificacion']
            correo = data['correo']
            telefono = data['telefono']
            contrato = data['contrato']
            horas = data['horas']
            pa = data['password']
            password = str(generate_password_hash(pa))
        
            peticion = f'INSERT INTO {tabla} VALUES (NULL, "{nombre}", "{apellido}", "{identificacion}", "{correo}", "{telefono}", "{contrato}", "{horas}", "{password}", 1)'
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






    return app

if __name__ == '__main__':
    app = createapp()
    app.run(port=8000)