from flask import flash, request
import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
import locale

class Create:
    def __init__(self):
        self.url = "http://127.0.0.1:8000/"
    #traer datos
    def get(self, tab):
        consulta = self.url+"consult/"
        api = requests.get(consulta+tab)
        data = api.json()
        return data
    # CONSULTAR DATOS DE UN ID ESPECIFICO
    def datos(self,id, col, tab):
        consulta = self.url+"consult/datos/"
        api = requests.get(consulta+id+"/"+col+"/"+tab)
        data = api.json()
        return data
    def todos(self,id, col, tab):
        consulta = self.url+"consult/todos/"
        api = requests.get(consulta+id+"/"+col+"/"+tab)
        data = api.json()
        return data
    def todas(self,id, col, tab):
        consulta = self.url+"consult/todas/"
        api = requests.get(consulta+id+"/"+col+"/"+tab)
        data = api.json()
        return data
    # se usa para consultar algo especifico en una tabla
    # d es dato consulta, t es tabla y c columna 
    def consultar(self, d, t, c):
        consult = self.url+"consult/espec/"
        useri = requests.get(consult+d+"/"+t+"/"+c)
        user = useri.json()
        return user
    # se usa para hacer consultas compuestas en una tabla especifica
    def group(self, ta, con1, da1, con2, da2):
        consulta = "http://127.0.0.1:8000/consult/group/"
        api = requests.get(consulta+ta+"/"+con1+"/"+da1+"/"+con2+"/"+da2)
        user = api.json()
        return user
    # sumar todos los resultados dando un numero
    def sumall(self, tab):
        consulta = self.url+"api/all/"
        api = requests.get(consulta+tab)
        data = api.json()
        return data
    # CONSULTAS CON JOIN
    def getJoin(self, tab1, tab2, dat1, dat2):
        consulta = self.url+"consult/jall/"
        api = requests.get(consulta+tab1+"/"+tab2+"/"+dat1+"/"+dat2)
        data = api.json()
        return data
    # CONSULTA JOIN CON DOS TABLAS
    def joinDos(self, dat, dat1, dat2, dat3, dat4, dat5, dat6, dat7):
        consulta = self.url+"consult/dos/"
        api = requests.get(consulta+dat+"/"+dat1+"/"+dat2+"/"+dat3+"/"+dat4+"/"+dat5+"/"+dat6+"/"+dat7)
        data = api.json()
        return data
    # CONSULTA JOIN CON TRES TABLAS
    def joinTres(self, dat, dat1, dat2, dat3, dat4, dat5, dat6, dat7, dat8, dat9, dat10):
        consulta = self.url+"consult/tres/"
        api = requests.get(consulta+dat+"/"+dat1+"/"+dat2+"/"+dat3+"/"+dat4+"/"+dat5+"/"+dat6+"/"+dat7+"/"+dat8+"/"+dat9+"/"+dat10)
        data = api.json()
        return data
    # CONSULTAR JOIN CON 4 TABLAS  
    def joinCua(self, dat, dat1, dat2, dat3, dat4, dat5, dat6, dat7, dat8, dat9, dat10, dat11, l,dat12, dat13, dat14):
        consulta = self.url+"consult/cua/"
        api = requests.get(consulta+dat+"/"+dat1+"/"+dat2+"/"+dat3+"/"+dat4+"/"+dat5+"/"+dat6+"/"+dat7+"/"+dat8+"/"+dat9+"/"+dat10+"/"+dat11+"/"+l+"/"+dat12+"/"+dat13+"/"+dat14)
        data = api.json()
        return data
    # CONSULTA JOIN CASCADA UNA VARIABLE, TABLA INICIAL
    def casJoin(self, tab1):
        consulta = self.url+"consult/cascada/"
        api = requests.get(consulta+tab1)
        data = api.json()
        return data

    #CREACION 
    # CREAR CENTROS
    def centros(self, nom, tel, descrip):
        url = self.url+"insertar/ce"
        centro = {
            'nombre': nom,
            'telefono': tel,
            'descripcion': descrip,
            'lugar': 'Centros'
        }
        user = self.consultar(nom,'Centros', 'Centro')
        
        if user == None:
            api = requests.post(url, json=centro)
            if api.status_code == 200:
                mensaje = f'El {nom} se registro correctamente'
                flash(mensaje, "success")
            else:
                mensaje = "a ocurrido un problema, no se pudo crear el centro.. intentalo de nuevo!"
                flash(mensaje, "error")
        else:
            mensaje = f'El {nom} ya existe'
            flash(mensaje)
    # CREAR SEDES
    def sedes(self, id_centro, nom, descrip):
        url = self.url+"insertar/se"
        sede = {
            'id_centro': id_centro,
            'nombre': nom,
            'descripcion': descrip,
            'lugar': 'Sedes'
            }
        user = self.consultar(nom, 'Sedes', 'Sede')
        if user == None:
            api = requests.post(url, json=sede)
            if api.status_code == 200:
                mensaje = f'La sede {nom} se registro correctamente'
                flash(mensaje, "success")
            else:
                mensaje = "a ocurrido un problema, no se pudo crear la sede.. intentalo de nuevo!"
                flash(mensaje, "error")
        else:
            mensaje = f'El {nom} ya existe'
            flash(mensaje)
    # CREAR AMBIENTES
    def ambientes(self, id_sede, nom, horas, descrip):
        url = self.url+"insertar/amb"
        ambi = {
            'id_sede': id_sede,
            'nombre': nom,
            'horas': horas,
            'descripcion': descrip,
            'lugar': 'Ambientes'
        }
        user = self.consultar(nom, 'Ambientes', 'Ambiente')
        if user == None:
            api = requests.post(url, json=ambi)
            if api.status_code == 200:
                mensaje = f'El ambiente {nom} se registro correctamente'
                flash(mensaje, "success")
            else:
                mensaje = "a ocurrido un problema, no se pudo crear el ambiente.. intentalo de nuevo"
                flash(mensaje, "error")
    # CREAR PROGRAMAS
    def programas(self, id_sede, nom, id_titu, descrip):
        url = self.url+"insertar/pro"
        programa = {
            'id_sede': id_sede,
            'nombre': nom,
            'id_titulo': id_titu,
            'descripcion': descrip,
            'lugar': 'Programas'
        }
        user = self.consultar(nom,'Programas', 'Programa')
        if user == None:
            api = requests.post(url, json=programa)
            if api.status_code == 200:
                mensaje = f'El programa {nom} se registro correctamente'
                flash(mensaje, "success")
            else:
                mensaje = "a ocurrido un problema, no se pudo crear el programa.. intentalo de nuevo!"
                flash(mensaje, "error")
        else:
            mensaje = f'El {nom} ya existe'
            flash(mensaje)
    # CREAR FICHAS
    def fichas(self, progra, ficha, descri):
        url = self.url+"insertar/fich"
        ficho = {
            'id_programa': progra,
            'ficha': ficha,
            'descripcion': descri,
            'lugar': 'Fichas'
        }
        user = self.consultar(ficha, 'Fichas', 'Ficha')
        if user == None:
            api = requests.post(url, json=ficho)
            if api.status_code == 200:
                mensaje = f'La ficha {ficha} se registro correctamente'
                flash(mensaje, "success")
            else:
                mensaje = "a ocurrido un problema, no se pudo crear el programa.. intentalo de nuevo!"
                flash(mensaje, "error")
        else:
            mensaje = f'La ficha {ficha} ya existe'
            flash(mensaje)
    #CREAR ACTIVIDADES
    def actividades(self, progra, nombre, horas, descri):
        url = self.url+"insertar/acti"
        activi = {
            'id_programa': progra,
            'nombre': nombre,
            'horas': horas,
            'descripcion': descri,
            'lugar': 'Actividades'
        }
        user = self.consultar(nombre, 'Actividades', 'Actividad')
        if user == None:
            api = requests.post(url, json=activi)
            if api.status_code == 200:
                mensaje = f'La actividad {nombre} se registro correctamente'
                flash(mensaje, "success")
            else:
                mensaje = "a ocurrido un problema, no se pudo crear el programa.. intentalo de nuevo!"
                flash(mensaje, "error")
        else:
            mensaje = f'La actividad {nombre} ya existe'
            flash(mensaje)
    # CREAR PROFESORES
    def docentes(self, centro, nombre, apellidos, identi, correo, contra, horas, paswd):
        url = self.url+"insertar/inst"
        docen = {
            'id_centro': centro,
            'nombre': nombre,
            'apellido': apellidos,
            'identi': identi,
            'correo': correo,
            'contra': contra,
            'horas': horas,
            'paswd': paswd,
            'lugar': 'Instructores'
        }
        user = self.consultar(identi, 'Instructores', 'NumIdenti')
        if user == None:
            api = requests.post(url, json=docen)
            if api.status_code == 200:
                mensaje = f'El docente {nombre} se registro correctamente'
                flash(mensaje, "success")
            else:
                mensaje = "a ocurrido un problema, no se pudo crear el programa.. intentalo de nuevo!"
                flash(mensaje, "error")
        else:
            mensaje = f'El docente {nombre} ya existe'
            flash(mensaje)

    # CARGA MASIVA
    #optener id
    def obtener_id(self, motor, nom, col, tab):
        col1= col.lower()
        #query = f"SELECT ID_{col1} FROM {tab} WHERE {col} = '{nom}'"
        consulta = self.url+"consult/idexcel/"
        s = self.url+f"{consulta}{nom}/{col}/{col1}/{tab}"
        print(s)
        api = requests.get(consulta+nom+"/"+col+"/"+col1+"/"+tab)
            # Verificar que la solicitud fue exitosa
        if api.status_code == 200:
            data = api.json()
            print(data)  # Imprimir los datos para ver su estructura
            
            # Asegurarte de que data es una lista y tiene al menos un elemento
            if isinstance(data, list) and len(data) > 0:
                return data[0]  # Retorna el primer elemento del arreglo
            else:
                raise ValueError(f"No se encontró un centro con el nombre: {nom}")
        else:
            raise ConnectionError(f"Error en la solicitud a la API: {api.status_code}")
    def obtener_ids(self, motor, nom, col, tab):
        col1= col.lower()
        col1 = col1+"s"
        #query = f"SELECT ID_{col1} FROM {tab} WHERE {col} = '{nom}'"
        consulta = self.url+"consult/idexcel/"
        s = self.url+f"{consulta}{nom}/{col}/{col1}/{tab}"
        print(s)
        api = requests.get(consulta+nom+"/"+col+"/"+col1+"/"+tab)
            # Verificar que la solicitud fue exitosa
        if api.status_code == 200:
            data = api.json()
            print(data)  # Imprimir los datos para ver su estructura
            
            # Asegurarte de que data es una lista y tiene al menos un elemento
            if isinstance(data, list) and len(data) > 0:
                return data[0]  # Retorna el primer elemento del arreglo
            else:
                raise ValueError(f"No se encontró un centro con el nombre: {nom}")
        else:
            raise ConnectionError(f"Error en la solicitud a la API: {api.status_code}")
    def obtener_titulo(self, motor, nom, col, tab):
        col1= 'titulo'
        #query = f"SELECT ID_{col1} FROM {tab} WHERE {col} = '{nom}'"
        consulta = self.url+"consult/idexcel/"
        s = self.url+f"{consulta}{nom}/{col}/{col1}/{tab}"
        print(s) 
        api = requests.get(consulta+nom+"/"+col+"/"+col1+"/"+tab)
            # Verificar que la solicitud fue exitosa
        if api.status_code == 200:
            data = api.json()
            print(data)  # Imprimir los datos para ver su estructura
            
            # Asegurarte de que data es una lista y tiene al menos un elemento
            if isinstance(data, list) and len(data) > 0:
                return data[0]  # Retorna el primer elemento del arreglo
            else:
                raise ValueError(f"No se encontró un centro con el nombre: {nom}")
        else:
            raise ConnectionError(f"Error en la solicitud a la API: {api.status_code}")

    def carga(self, file, tab):
        db = 'sqlite:///./api/sena.db'
        if tab == 'Centros':
            df = pd.read_excel(file,sheet_name="Hoja4", skiprows=2, index_col=0)
            print(df)
            motor = create_engine(db)
            df.to_sql(tab, con=motor, if_exists='append', index=False)
            print('carga exitosa')
            flash("carga exitosa", "success")
        elif tab == "prueba":
            pass
        else:
            print("paso algo malo")
    def carga_id(self, file, tab, c, t):
            db = 'sqlite:///./api/sena.db'
            motor = create_engine(db)
            if tab == 'Sedes':
                # Leer el archivo Excel
                df = pd.read_excel(file, sheet_name="Hoja2", skiprows=3)
                print(df.head())  # Verificar las primeras filas
                print(df.columns)  # Verificar los nombres de las columnas
                # Normalizar nombres de columnas
                df.columns = df.columns.str.strip().str.upper()  # Quitar espacios y pasar a mayúsculas
                # Verificar si las columnas necesarias están presentes
                required_columns = ['CENTROS', 'SEDES', 'DESCRIPCION']
                for col in required_columns:
                    if col not in df.columns:
                        raise KeyError(f"Falta la columna {col} en el DataFrame")
                # Obtener centros únicos
                centros_unicos = df['CENTROS'].unique()
                print(f"Centros únicos: {centros_unicos}")

                # Obtener ids de centros
                ids_centros = {}
                for nombre in centros_unicos:
                    try:
                        ids_centros[nombre] = self.obtener_id(motor, nombre, c, t)
                    except ValueError as e:
                        print(f"Error al obtener ID para {nombre}: {e}")

                print(f"IDs de centros: {ids_centros}")

                # Reemplazar la columna CENTROS con los id_centro
                df['CENTROS'] = df['CENTROS'].map(ids_centros)

                # Verificar si hay valores NaN (centros no encontrados)
                if df['CENTROS'].isnull().any():
                    print("Algunos centros no se encontraron. Verifica los nombres.")
                
                # Crear nuevo DataFrame para insertar
                data_to_insert = {
                    'id_centro': df['CENTROS'],  # Asignar directamente los ids
                    'Sede': df['SEDES'],  # Asigna directamente la columna SEDES
                    'descripcion': df['DESCRIPCION']  # Asigna directamente la columna DESCRIPCION
                }

                # Crear un DataFrame con los datos a insertar
                df_to_insert = pd.DataFrame(data_to_insert)

                # Insertar datos en la tabla
                df_to_insert.to_sql('Sedes', con=motor, if_exists='append', index=False)
                print('Carga exitosa con id_centro incluido.')
                flash("carga exitosa", "success")
            elif tab == 'Ambientes':
                # Leer el archivo Excel
                df = pd.read_excel(file, sheet_name="Hoja5", skiprows=3)
                print(df.head())
                print(df.columns)
                # Normalizar nombres de columnas
                df.columns = df.columns.str.strip().str.upper()

                required_columns = ['CENTRO', 'SEDE', 'AMBIENTE', 'HORAS DIARIAS', 'DESCRIPCION']
                for col in required_columns:
                    if col not in df.columns:
                        raise KeyError(f"Falta la columna {col} en el DataFrame")

                centros_unicos = df['CENTRO'].unique()
                print(f"Centros únicos: {centros_unicos}")
                
                sedes_unicas = df['SEDE'].unique()
                print(f"Sedes únicas: {sedes_unicas}")
                # Obtener id de centros y sedes
                ids_centros = {}
                ids_sedes = {}
                
                for nombre in centros_unicos:
                    try:
                        ids_centros[nombre] = self.obtener_id(motor, nombre, 'Centro', 'Centros')
                    except ValueError as e:
                        print(f"Error al obtener ID para el centro {nombre}: {e}")

                for sede in sedes_unicas:
                    try:
                        ids_sedes[sede] = self.obtener_ids(motor, sede, c, t)
                    except ValueError as e:
                        print(f"Error al obtener ID para la sede {sede}: {e}")

                # Reemplazar las columnas con los id_centro y id_sede
                df['CENTRO'] = df['CENTRO'].map(ids_centros)
                df['SEDE'] = df['SEDE'].map(ids_sedes)
                # Verificar si hay valores NaN (centros o sedes no encontrados)
                if df['CENTRO'].isnull().any() or df['SEDE'].isnull().any():
                    print("Algunos centros o sedes no se encontraron. Verifica los nombres.")
                # Crear nuevo DataFrame para insertar en la tabla intermedia
                data_to_insert = {
                    #'id_centro': df['CENTRO'],
                    'id_sede': df['SEDE'],
                    'Ambiente': df['AMBIENTE'],
                    'HorasDia': df['HORAS DIARIAS'],
                    'HorasAsig': 0,
                    'descripcion': df['DESCRIPCION']
                }
                # Crear un DataFrame con los datos a insertar
                df_to_insert = pd.DataFrame(data_to_insert)
                df_to_insert.to_sql('Ambientes', con=motor, if_exists='append', index=False)
                print('Carga exitosa con ambiente y id_sede incluidos.')
                flash("carga exitosa", "success")
            elif tab == 'Programas':
                df = pd.read_excel(file, sheet_name="Hoja3", skiprows=3)
                print(df.head())
                print(df.columns)
                # Normalizar nombres de columnas
                df.columns = df.columns.str.strip().str.upper()

                required_columns = ['CENTRO', 'SEDE', 'PROGRAMA', 'TITULACION', 'DESCRIPCION']
                for col in required_columns:
                    if col not in df.columns:
                        raise KeyError(f"Falta la columna {col} en el DataFrame")

                centros_unicos = df['CENTRO'].unique()
                print(f"Centros únicos: {centros_unicos}")
                
                sedes_unicas = df['SEDE'].unique()
                print(f"Sedes únicas: {sedes_unicas}")

                titulaciones_unicas = df['TITULACION'].unique()
                print(f"titulaciones únicas: {titulaciones_unicas}")
                # Obtener id de centros y sedes
                ids_centros = {}
                ids_sedes = {}
                ids_titulacion = {}
                
                for nombre in centros_unicos:
                    try:
                        ids_centros[nombre] = self.obtener_id(motor, nombre, 'Centro', 'Centros')
                    except ValueError as e:
                        print(f"Error al obtener ID para el centro {nombre}: {e}")

                for sede in sedes_unicas:
                    try:
                        ids_sedes[sede] = self.obtener_ids(motor, sede, c, t)
                    except ValueError as e:
                        print(f"Error al obtener ID para la sede {sede}: {e}")
                
                for titulo in titulaciones_unicas:
                    try:
                        ids_titulacion[titulo] = self.obtener_titulo(motor, titulo, 'Titulacion', 'Titulaciones')
                    except ValueError as e:
                        print(f"Error al obtener ID para la sede {titulo}: {e}")

                # Reemplazar las columnas con los id_centro y id_sede
                df['CENTRO'] = df['CENTRO'].map(ids_centros)
                df['SEDE'] = df['SEDE'].map(ids_sedes)
                df['TITULACION'] = df['TITULACION'].map(ids_titulacion)
                # Verificar si hay valores NaN (centros o sedes no encontrados)
                if df['CENTRO'].isnull().any() or df['SEDE'].isnull().any() or df['TITULACION'].isnull().any():
                    print("Algunos centros o sedes no se encontraron. Verifica los nombres.")
                # Crear nuevo DataFrame para insertar en la tabla intermedia
                data_to_insert = {
                    #'id_centro': df['CENTRO'],
                    'id_sede': df['SEDE'],
                    'Programa': df['PROGRAMA'],
                    'id_titulacion': df['TITULACION'],
                    'descripcion': df['DESCRIPCION']
                }
                # Crear un DataFrame con los datos a insertar
                df_to_insert = pd.DataFrame(data_to_insert)
                df_to_insert.to_sql('Programas', con=motor, if_exists='append', index=False)
                print('Carga exitosa con id_centro y id_sede incluidos.')
                flash("carga exitosa", "success")
            elif tab == 'Instructores':
                # Leer el archivo Excel
                df = pd.read_excel(file, sheet_name="Hoja6", skiprows=3)
                print(df.head())  # Verificar las primeras filas
                print(df.columns)  # Verificar los nombres de las columnas
                # Normalizar nombres de columnas
                df.columns = df.columns.str.strip().str.upper()  # Quitar espacios y pasar a mayúsculas
                # Verificar si las columnas necesarias están presentes
                required_columns = ['CENTRO', 'NOMBRE', 'APELLIDO', 'NUMERO IDENTIFICACION', 'CORREO', 'CONTRATO', 'HORAS SEMANA', 'HORAS ASIG', 'CONTRASEÑA']
                for col in required_columns:
                    if col not in df.columns:
                        raise KeyError(f"Falta la columna {col} en el DataFrame")
                # Obtener centros únicos
                centros_unicos = df['CENTRO'].unique()
                print(f"Centros únicos: {centros_unicos}")

                # Obtener ids de centros
                ids_centros = {}
                for nombre in centros_unicos:
                    try:
                        ids_centros[nombre] = self.obtener_id(motor, nombre, c, t)
                    except ValueError as e:
                        print(f"Error al obtener ID para {nombre}: {e}")

                print(f"IDs de centros: {ids_centros}")
                # Reemplazar la columna CENTRO con los id_centro
                df['CENTRO'] = df['CENTRO'].map(ids_centros)

                # Verificar si hay valores NaN (centros no encontrados)
                if df['CENTRO'].isnull().any():
                    print("Algunos centros no se encontraron. Verifica los nombres.")

                # Crear nuevo DataFrame para insertar
                data_to_insert = {
                    'id_centro': df['CENTRO'],
                    'Nombre': df['NOMBRE'], 
                    'Apellido' : df['APELLIDO'], 
                    'NumIdenti': df['NUMERO IDENTIFICACION'], 
                    'Correo': df['CORREO'], 
                    'Tipocontrato': df['CONTRATO'], 
                    'HorasTotal': df['HORAS SEMANA'], 
                    'HorasAsig': df['HORAS ASIG'], 
                    'Password': df['CONTRASEÑA']
                }
                # Crear un DataFrame con los datos a insertar
                df_to_insert = pd.DataFrame(data_to_insert)

                # Insertar datos en la tabla
                df_to_insert.to_sql('Instructores', con=motor, if_exists='append', index=False)
                print('Carga exitosa con id_centro incluido.')
                flash("carga exitosa", "success")
            elif tab == 'Fichas':
                # Leer el archivo Excel
                df = pd.read_excel(file, sheet_name="Hoja7", skiprows=3)
                print(df.head())  # Verificar las primeras filas
                print(df.columns)  # Verificar los nombres de las columnas
                # Normalizar nombres de columnas
                df.columns = df.columns.str.strip().str.upper()  # Quitar espacios y pasar a mayúsculas
                # Verificar si las columnas necesarias están presentes
                required_columns = ['PROGRAMA', 'FICHA', 'DESCRIPCION']
                for col in required_columns:
                    if col not in df.columns:
                        raise KeyError(f"Falta la columna {col} en el DataFrame")
                # Obtener centros únicos
                programas_unicos = df['PROGRAMA'].unique()
                print(f"Centros únicos: {programas_unicos}")

                 # Obtener ids de centros
                ids_programas = {}
                for nombre in programas_unicos:
                    try:
                        ids_programas[nombre] = self.obtener_id(motor, nombre, c, t)
                    except ValueError as e:
                        print(f"Error al obtener ID para {nombre}: {e}")

                print(f"IDs de centros: {ids_programas}")

                 # Reemplazar la columna PROGRAMA con los id_centro
                df['PROGRAMA'] = df['PROGRAMA'].map(ids_programas)

                # Verificar si hay valores NaN (centros no encontrados)
                if df['PROGRAMA'].isnull().any():
                    print("Algunos programas no se encontraron. Verifica los nombres.")
                
                # Crear nuevo DataFrame para insertar
                data_to_insert = {
                    'id_programa': df['PROGRAMA'],  # Asignar directamente los ids
                    'Ficha': df['FICHA'],  # Asigna directamente la columna SEDES
                    'Descripcion': df['DESCRIPCION']  # Asigna directamente la columna DESCRIPCION
                }
                 # Crear un DataFrame con los datos a insertar
                df_to_insert = pd.DataFrame(data_to_insert)

                # Insertar datos en la tabla
                df_to_insert.to_sql('Fichas', con=motor, if_exists='append', index=False)
                print('Carga exitosa con id_programa incluido.')
            elif tab == 'Actividades':
                # Leer el archivo Excel
                df = pd.read_excel(file, sheet_name="Hoja8", skiprows=3)
                print(df.head())  # Verificar las primeras filas
                print(df.columns)  # Verificar los nombres de las columnas
                # Normalizar nombres de columnas
                df.columns = df.columns.str.strip().str.upper()  # Quitar espacios y pasar a mayúsculas
                # Verificar si las columnas necesarias están presentes
                required_columns = ['PROGRAMA', 'ACTIVIDAD', 'HORAS TOTAL', 'HORAS ASIG', 'DESCRIPCION']
                for col in required_columns:
                    if col not in df.columns:
                        raise KeyError(f"Falta la columna {col} en el DataFrame")
                # Obtener centros únicos
                programas_unicos = df['PROGRAMA'].unique()
                print(f"Centros únicos: {programas_unicos}")

                 # Obtener ids de centros
                ids_programas = {}
                for nombre in programas_unicos:
                    try:
                        ids_programas[nombre] = self.obtener_id(motor, nombre, c, t)
                    except ValueError as e:
                        print(f"Error al obtener ID para {nombre}: {e}")

                print(f"IDs de centros: {ids_programas}")

                 # Reemplazar la columna PROGRAMA con los id_centro
                df['PROGRAMA'] = df['PROGRAMA'].map(ids_programas)

                # Verificar si hay valores NaN (centros no encontrados)
                if df['PROGRAMA'].isnull().any():
                    print("Algunos programas no se encontraron. Verifica los nombres.")
                
                # Crear nuevo DataFrame para insertar
                data_to_insert = {
                    'id_programa': df['PROGRAMA'],  # Asignar directamente los ids
                    'Actividad': df['ACTIVIDAD'],
                    'HorasTotal': df['HORAS TOTAL'],
                    'HorasAsig': df['HORAS ASIG'],
                    'Descripcion': df['DESCRIPCION']  # Asigna directamente la columna DESCRIPCION
                }
                 # Crear un DataFrame con los datos a insertar
                df_to_insert = pd.DataFrame(data_to_insert)

                # Insertar datos en la tabla
                df_to_insert.to_sql('Actividades', con=motor, if_exists='append', index=False)
                print('Carga exitosa con id_programa incluido.')
                flash("carga exitosa", "success")

    # ACTUALIZACIONES
    # ACTUALIZAR CENTRO, FICHAS, SEDES
    def actualcen(self, tab, nom, tel, des, id, nom1, tel1, des1, id1):
        link = self.url+"update/t/"
        print(link+tab+"/"+nom+"/"+tel+"/"+des+"/"+id+"/"+nom1+"/"+tel1+"/"+des1+"/"+id1)
        api = requests.put(link+tab+"/"+nom+"/"+tel+"/"+des+"/"+id+"/"+nom1+"/"+tel1+"/"+des1+"/"+id1)
        print(f"Status Code: {api.status_code}")
        print(f"Response: {api.text}")
        if api.status_code == 200:
            mensaje = f'Se actualizo correctamente.'
            print(mensaje)
            flash(mensaje, "success")
        else:
            mensaje = "a ocurrido un problema, no se pudo actualizar."
            print(mensaje)
            flash(mensaje, "error")
    # ACTUALIZAR INSTRUCTOR
    def actualin(self, centro, nombre, apellidos, identi, correo, contra, horas, id):
        link = self.url+"update/in/"
        api = requests.put(link+centro+"/"+nombre+"/"+apellidos+"/"+identi+"/"+correo+"/"+contra+"/"+horas+"/"+id)
        print(f"Status Code: {api.status_code}")
        print(f"Response: {api.text}")
        if api.status_code == 200:
            mensaje = f'Se actualizo correctamente.'
            print(mensaje)
            flash(mensaje, "success")
        else:
            mensaje = "a ocurrido un problema, no se pudo actualizar."
            print(mensaje)
            flash(mensaje, "error")
    # ACTUALIZAR ACTIVIDADES, ADMIN, AMBIENTE
    def actualact(self, a, id_programa, actividad, hor, id_actividades, descri, progra, nom, horas, des, id):
        link = self.url+"update/act/"
        queri = f'{link}{a}/{id_programa}/{actividad}/{hor}/{id_actividades}/{descri}/{progra}/{nom}/{horas}/{des}/{id}'
        #api = requests.put(link+a+"/"+id_programa+"/"+actividad+"/"+hor+"/"+id_actividades+"/"+descri+"/"+progra+"/"+nom+"/"+horas+"/"+des+"/"+id)
        print(queri)
        api = requests.put(queri)
        print(f"Status Code: {api.status_code}")
        print(f"Response: {api.text}")
        if api.status_code == 200:
            mensaje = f'Se actualizo correctamente.'
            print(mensaje)
            flash(mensaje, "success")
        else:
            mensaje = "a ocurrido un problema, no se pudo actualizar."
            print(mensaje)
            flash(mensaje, "error")

    # ACTUALIZAR SOLO ACTIVIDADES
    def actualacti(self, progra, nombre, horas, descri, id):
        link = self.url+"update/acti/"
        api = requests.put(link+progra+"/"+nombre+"/"+horas+"/"+descri+"/"+id)
        if api.status_code == 200:
            mensaje = f'Se actualizo correctamente.'
            print(mensaje)
            flash(mensaje, "success")
        else:
            mensaje = "a ocurrido un problema, no se pudo actualizar."
            print(mensaje)
            flash(mensaje, "error")
    # ACTUALIZAR SEDE
    def actualsed(self, cen, nom, des, id):
        link = self.url+"update/sed/"
        api = requests.put(link+cen+"/"+nom+"/"+des+"/"+id)
        if api.status_code == 200:
            mensaje = f'Se actualizo correctamente.'
            print(mensaje)
            flash(mensaje, "succes")
        else:
            mensaje = "a ocurrido un problema, no se pudo actualizar."
            print(mensaje)
            flash(mensaje, "error")
    # ACTUALIZAR AMBIENTE
    def actualambi(self, sede, nom, horas, des, id):
        link = self.url+"update/ambi/"
        que = f"{link}{sede}/{nom}/{horas}/{des}/{id}"
        print(que)
        api = requests.put(link+sede+"/"+nom+"/"+horas+"/"+des+"/"+id)
        if api.status_code == 200:
            mensaje = f'Se actualizo correctamente.'
            print(mensaje)
            flash(mensaje, "succes")
        else:
            mensaje = "a ocurrido un problema, no se pudo actualizar."
            print(mensaje)
            flash(mensaje, "error")
    # ACTUALIZAR PROGRAMAS
    def actualpro(self, sede, progra, titulo, descri, id):
        link = self.url+"update/pro/"
        api = requests.put(link+sede+"/"+progra+"/"+titulo+"/"+descri+"/"+id)
        if api.status_code == 200:
            mensaje = f'Se actualizo correctamente.'
            print(mensaje)
            flash(mensaje, "success")
        else:
            mensaje = "a ocurrido un problema, no se pudo actualizar."
            print(mensaje)
            flash(mensaje, "error")
    #  ACTUALIZAR  FICHAS
    def actualfich(self, progra, ficha, descri, id):
        link = self.url+"update/ficha/"
        api = request.put(link+progra+"/"+ficha+"/"+descri+"/"+id)
        if api.status_code == 200:
            mensaje = f'Se actualizó correctamente.'
            print(mensaje)
            flash(mensaje, "success")
        else:
            mensaje = "a ocurrido un problema, no se pudo actualizar."
            print(mensaje)
            flash(mensaje, "error") 
    # ACTUALIZAR PERFIL
    def actualper(self, nombre, apellido, identi, correo, id):
        link = self.url+"update/perf/"
        api = requests.put(link+id+"/"+nombre+"/"+apellido+"/"+identi+"/"+correo)
        if api.status_code == 200:
            mensaje = f'Se actualizo correctamente.'
            print(mensaje)
            flash(mensaje, "success")
        else:
            mensaje = "a ocurrido un problema, no se pudo actualizar."
            print(mensaje)
            flash(mensaje, "error")
    
    
    
    # AGREGAR BLOQUE DE HORARIO  
    def horr(self, cen, sed, ambi, ins, pro, fi, ma, datos):
        url = self.url+"confi/crear/horacal"
        linkHoras = self.url+"calc/"
        horasT = len(datos)
        horarios = []
        for i in range(len(datos)):
            dia = datos[i][2]
            hora = datos[i][1]
            bloId = datos[i][0]
            horario = {
                'centro': cen,
                'sede': sed,
                'programa': pro,
                'instructor': ins,
                'salon': ambi,
                'ficha': fi,
                'acti': ma,
                'horas': hora,
                'dias': dia,
                'id': bloId
            }
            horarios.append(horario)
        print(horarios)
        inf = self.verificacion(horarios, horasT)
        if inf == None:
            # GUARDADO DE DATOS LIMPIO
            for i in range(len(datos)):
                dia = datos[i][2]
                hora = datos[i][1]
                bloId = datos[i][0]
                horario = {
                    'centro': cen,
                    'sede': sed,
                    'programa': pro,
                    'instructor': ins,
                    'salon': ambi,
                    'ficha': fi,
                    'acti': ma,
                    'horas': hora,
                    'dias': dia,
                    'id': bloId
                }
                # GUARDAR INFORMACION   
                calendar = requests.post(url, json=horario)
                if calendar.status_code == 200 or calendar == "realizado":
                    hTotales = str(len(datos))
                    ins = str(ins)
                    ma = str(ma)
                    fi = str(fi)
                    uul = self.url+"agre/dual/"
                    envioHoras = uul+ins+"/"+hTotales+"/"+ma+"/"+fi
                    resultT = requests.post(envioHoras)
                    print(resultT)
                    print('El horario se creo correctamente')
                    mensaje = "El horario se creo correctamente"
                    flash(mensaje, "success")
                else:
                    print('Error al crear el horario.. estamos en la 801')
                    mensaje = "a ocurrido un problema, no se pudo crear el horario.. intentalo de nuevo!"
                    flash(mensaje, "info")
        else:
            mensaje = inf[0]
            print(mensaje)
            flash(mensaje, "error")
    # VERIFICAR LOS DATOS, HORAS Y CRUCES
    def verificacion(self, horarios, horasT):
        print("estamos en verificacion")
        respuesta = []
        for h in horarios:
            ins = h['instructor']
            sede = h['sede']
            ambi =  h['salon']
            fi = h['ficha']
            ma = h['acti']
            dia = h['dias']
            hora = h['horas']
            id =  h['id']
            link = self.url+"comp/"
            horasT = str(horasT)
            consulta = link+ambi+"/"+id+"/"+ins+"/"+sede+"/"+fi+"/"+ma+"/"+hora+"/"+dia
            consul = requests.get(consulta)
            inf = consul.json()
            respuesta.append(inf)
        
        info = "None"
        for r in respuesta:
            if r == None:
                info = None
                print(info)
                
            else:
                print(r[0])
                info = r
                break
        return info
            
    # EXCEL DOS METODOS POR AHORA
    # INSTRUCTOR
    def excelIns(self, id, col, tab):
        # traer datos del profe
        profe = self.datos(id, col, tab)
        id = str(profe[0])
        name = str(profe[2])
        ape = str(profe[3])
        # traer los horarios del id del profesor
        registros = self.todos(id, "id_instructor", "Bloques")
        datos_excel = []
        # agregamos tuplas a la lista con los datos de cada registro de bloques
        for re in registros:
            dia = str(re[3])
            ini = int((re[1]) / 60)
            fin = int((re[2] + 1) / 60)
            fi = str(re[4])
            locale.setlocale(locale.LC_TIME, 'es_ES')
            fecha = datetime.strptime(dia, '%Y-%m-%d')
            dia_semana = fecha.strftime('%A')
            datos_excel.append((name, ape, dia, dia_semana, ini, fin, fi))
        print(datos_excel)
        return datos_excel
    # FICHAS
    def excelFich(self, id, col, tab):
        # traer datos del profe
        ficha = self.datos(id, col, tab)
        id = str(ficha[0])
        name = str(ficha[2])
        # traer los horarios del id del profesor
        registros = self.todas(id, "id_ficha", "Bloques")
        print("fichas:")
        print(registros)
        datos_excel = []
        # agregamos tuplas a la lista con los datos de cada registro de bloques
        for re in registros:
            dia = str(re[3])
            ini = int((re[1]) / 60)
            fin = int((re[2] + 1) / 60)
            fi = str(re[4])
            ape = str(re[5])
            locale.setlocale(locale.LC_TIME, 'es_ES')
            fecha = datetime.strptime(dia, '%Y-%m-%d')
            dia_semana = fecha.strftime('%A')
            datos_excel.append((name, dia, dia_semana, ini, fin, fi, ape))
        print(datos_excel)
        return datos_excel
    def valores_unicos(self, array, posicion):
        # Crear un conjunto (set) para almacenar los valores únicos
        valores_unicos = set()
        for elemento in array:
            valores_unicos.add(elemento[posicion])
        return list(valores_unicos)
    
    def fechas_de_la_semana(self):
        # Obtener la fecha actual
        hoy = datetime.now()
        # Calcular el inicio de la semana (lunes)
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        # Crear una lista de fechas de la semana
        fechas = [(inicio_semana + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(6)]
        return fechas