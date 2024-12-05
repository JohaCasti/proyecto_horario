import json
import mysql.connector
import sqlite3

#manejo de los query
class Query:

    # def database(self):
    #     con = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         password="",
    #         database="horarios",
    #         port=3306
    #     )
    #     self.con = con
    #     return con

    
    def database(self):
        con = sqlite3.connect("sena.db")
        self.con = con
        return con
    
    def conexion(self):
        con = self.database()
        cur = con.cursor()
        return cur
    
    #query para agregar actualizar o elimitar! 
    def Ejecutar(self,sql): 
        db = self.database()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        return json.dumps("realizado")

    # query para consultar varios
    def EjecutarQuery(self, sql):
        cursor = self.conexion()
        cursor.execute(sql)
        row=cursor.fetchall()
        return json.dumps(row)
    
    # query para consultar uno
    def EjecutarUno(self, sql):
        cursor = self.conexion()
        cursor.execute(sql)
        row=cursor.fetchone()
        return json.dumps(row)
    
    # query trae la tupla sin ser jsonÑ
    def consultApi(self, sql):
        cursor = self.conexion()
        cursor.execute(sql)
        row = cursor.fetchone()
        cursor.connection.close()
        return row