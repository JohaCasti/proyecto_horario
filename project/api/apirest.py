from flask import Flask, request, Blueprint
import json
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Query
"""""
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="horarios",
    port=3306
)
cursor = con.cursor()
#query para agregar actualizar o elimitar! 
def Ejecutar(sql,argumento=""): 
    cursor=con.cursor()
    cursor.execute(sql) 
    con.commit()
    return json.dumps("200 bare")

# query para consultar
def EjecutarQuery(sql):
    cursor.execute(sql)
    row=cursor.fetchall()
    return json.dumps(row)
"""""
apirest = Blueprint('consult', __name__, url_prefix='/consultapi')

@apirest.route('/list')
def listar():
    sql="SELECT * FROM admin"
    l = Query()
    x = l.EjecutarQuery(sql)
    return x


@apirest.route('/f/<id>')
def first(id):
    sql="SELECT * FROM instructor where id_instructor ="+id
    f = Query()
    x = f.EjecutarQuery(sql)
    return x

@apirest.route("/regisadmin",methods=['POST'])
def regisAdmin():
    # http://127.0.0.1:5000/consult/regisadmin
    data=request.get_json()  
    nombre = data['name']
    apellido = data['apellido']
    telefono = data['telefono']
    tipo_admin = data['tipo_admin']
    username = data['username']
    password = data['password']
    passwd = generate_password_hash(password)
    sql="INSERT INTO admin(Nombre, Apellido, Telefono, Tipo_admin, Username, Password) VALUES ('"+nombre+"','"+apellido+"','"+telefono+"','"+tipo_admin+"','"+username+"','"+passwd+"')"
    r = Query()
    result = r.Ejecutar(sql)
    return result