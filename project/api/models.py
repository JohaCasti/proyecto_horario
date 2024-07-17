import json
import mysql.connector

#manejo de los query
class Query:

    def database(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="horarios",
            port=3306
        )
        self.con = con
        return con
    
    def conexion(self):
        con = self.database()
        cur = con.cursor()
        return cur
    
    #query para agregar actualizar o elimitar! 
    def Ejecutar(self,sql,argumento=""): 
        cursor= self.conexion()
        cursor.execute(sql)
        con = self.database()
        con.commit()
        return json.dumps("200 bare")

    # query para consultar
    def EjecutarQuery(self, sql):
        cursor = self.conexion()
        cursor.execute(sql)
        row=cursor.fetchall()
        return json.dumps(row)
