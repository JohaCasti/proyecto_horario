from flask import flash, request
import requests


class Create:

    # se usa para consultar algo especifico en una tabla
    # d es dato consulta, t es tabla y c columna 
    def consultar(self, d, t, c):
        consult = "http://127.0.0.1:8000/consult/espec/"
        useri = requests.get(consult+d+"/"+t+"/"+c)
        user = useri.json()
        return user
    
    # se usa para hacer consultas compuestas en una tabla especifica
    def group(self, ta, con1, da1, con2, da2):
        consulta = "http://127.0.0.1:8000/consult/group/"
        api = requests.get(consulta+ta+"/"+con1+"/"+da1+"/"+con2+"/"+da2)
        user = api.json()
        return user

    #traer datos
    def get(self, tab):
        consulta = "http://127.0.0.1:8000/consult/"
        api = requests.get(consulta+tab)
        data = api.json()
        return data
    


    # traer con join del otro lado de la tabla del forykey
    # SELECT p.id_programa, p.Nombre, p.descripcion, c.nombre
    # FROM programas AS p
    # LEFT JOIN centro AS c ON p.centro=c.id_centro
    def getJoin(self, tab1, tab2, dat1, dat2):
        consulta = "http://127.0.0.1:8000/consult/left/"  #<tab1>/<tab2>/<dato1>/<dato2>
        api = requests.get(consulta+tab1+"/"+tab2+"/"+dat1+"/"+dat2)
        data = api.json()
        return data
    
    # join para solo ver un dato
    def joinUnDate(self, con, tab1, tab2, dat1, dat2, dat3, dat4):
        url = "http://127.0.0.1:8000/consult/joinespecif/"
        api = requests.get(url+con+"/"+tab1+"/"+tab2+"/"+dat1+"/"+dat2+"/"+dat3+"/"+dat4)
        data = api.json()
        print(data)
        return data
    

    # consulta 
    def datos(self,id, col, tab):
        consulta = "http://127.0.0.1:8000/consult/datos/"
        api = requests.get(consulta+id+"/"+col+"/"+tab)
        data = api.json()
        return data
    
    # sumar datos
    def sumall(self, tab):
        consulta = "http://127.0.0.1:8000/api/all/"
        api = requests.get(consulta+tab)
        data = api.json()
        return data

    # CREACION DE DATOS!!!!

    # crear centros
    def centros(self, nom, tel, descrip):
        url = "http://127.0.0.1:8000/consult/insertar/ce"
        centro = {
            'nombre': nom,
            'telefono': tel,
            'descripcion': descrip,
            'lugar': 'centro'
        }
        user = self.consultar(nom,'centro', 'Nombre')
        
        if user == None:
            api = requests.post(url, json=centro)
            if api.status_code == 200:
                mensaje = f'El {nom} se registro correctamente'
                flash(mensaje)
            else:
                mensaje = "a ocurrido un problema, no se pudo crear el centro.. intentalo de nuevo!"
                flash(mensaje)
        else:
            mensaje = f'El {nom} ya existe'
            flash(mensaje) 

    
    # crear instructor
    def instructores(self, nom, ape, ide, mail, tel, contra, horas, passwd):
        url = "http://127.0.0.1:8000/consult/insertar/pr"
        porfe = {
            'nombre': nom,
            'apellidos': ape,
            'identificacion': ide,
            'correo': mail,
            'telefono': tel,
            'contrato': contra,
            'horas': horas,
            'password': passwd,
            'lugar': 'instructor'
        }

        user = self.consultar(ide, 'instructor', 'Identificacion')

        if user == None:
            api = requests.post(url, json=porfe)
            if api.status_code == 200:
                mensaje = f'El instructor {nom} {ape} se registro correctamente'
                flash(mensaje)
            else:
                mensaje = "a ocurrido un problema, no se pudo crear el instructor.. intentalo de nuevo!"
                flash(mensaje)
        else:
            mensaje = f'El instructor {nom} {ape} ya esta registrado'
            flash(mensaje)

    #crear salones
    def salones(self, cen, num, des):
        url = "http://127.0.0.1:8000/consult/insertar/sa"
        salon = {
            'centro': cen,
            'numero': num,
            'descripcion': des,
            'lugar': 'salon'
        }

        user = self.group('salon', 'Centro', cen, 'Salon', num)
        if user == None:
            api = requests.post(url, json=salon)
            if api.status_code == 200:
                mensaje = f'El salon {num} del {cen} se registro correctamente'
                flash(mensaje)
            else:
                mensaje = "a ocurrido un problema, no se pudo crear el salon.. intentalo de nuevo!"
                flash(mensaje)
        else:
            mensaje = f'El salon {num} del {cen} ya esta registrado, intenta otro salon u otro centro!!'
            flash(mensaje)


    # creacion ficha
    def fichas(self, num, prog, ins, des):
        url = "http://127.0.0.1:8000/consult/insertar/fi"
        salon = {
            'ficha': num,
            'programa': prog,
            'instructor': ins,
            'descripcion': des,
            'lugar': 'ficha'
        }

        user = self.consultar(num, 'ficha', 'Num_ficha')
        if user == None:
            api = requests.post(url, json=salon)
            if api.status_code == 200:
                mensaje = f'La ficha {num} se registro correctamente'
                flash(mensaje)
            else:
                mensaje = "a ocurrido un problema, no se pudo crear la ficha.. intentalo de nuevo!"
                flash(mensaje)
        else:
            mensaje = f'La ficha {num} ya esta registrado'
            flash(mensaje)

            
    # crear programa
    def programa(self, nom, des, cen):
        url = "http://127.0.0.1:8000/consult/insertar/pro"
        programa = {
            'Nombre': nom,
            'descri': des,
            'centro': cen,
            'lugar': 'programas'
        }

        consult = self.joinUnDate('Nombre','programas','centro', 'centro','id_centro', cen, 'centro')
        print('ombre')
        print(consult)

        user = self.group('programas','Nombre', nom, 'centro', cen)
        if user == None:
            api = requests.post(url, json=programa)
            if api.status_code == 200:
                mensaje = f'El porgrama {nom} se registro correctamente'
                flash(mensaje)
            else:
                mensaje = "a ocurrido un problema, no se pudo crear el programa de formacion.. intentalo de nuevo!"
                flash(mensaje)
        else:
            mensaje = f'El programa {nom} del {consult[0][0]} ya esta registrado, intenta otro programa u otro centro!'
            flash(mensaje)



    # CREAR HORARIOS SIN CRUCE....
    def horarios(self, start, end, hori, horaf, cen, ins, sal, ficha, color, datos):
        url = "http://127.0.0.1:8000/consult/ingre/hori"
        horario = {
            'start': start,
            'end': end,
            'hora_i': hori,
            'hora_f': horaf,
            'centro': cen,
            'instructor': ins,
            'salon': sal,
            'ficha': ficha,
            'color': color,
            'datos': datos
        }
        consulta = "http://127.0.0.1:8000/consult/cruce/"
        datos = f"{cen}/{ins}/{sal}/{ficha}/{start}/{hori}/{end}/{horaf}"
        api = requests.get(consulta+datos)
        user = api.json()
            
        if user == None:
            print('aqui vamos')
        else:
            print(user)







    # ACTUALIZAR DATOS
    # actualizar centro
    def actualcen(self, tab, nom, tel, des, id):
        url = "http://127.0.0.1:8000/update/centroall/"
        api = requests.put(url+tab+"/"+nom+"/"+tel+"/"+des+"/"+id)
        
        if api.status_code == 200:
            mensaje = f'El centro fue actualizado.'
            flash(mensaje)
        else:
            mensaje = "a ocurrido un problema, no se pudo actualizar la informacion del centro."
            flash(mensaje)

    # actualizar programas
    def actualpro(self, tab, nom, tel, des, id):
        url = "http://127.0.0.1:8000/update/programall/"
        #user = self.group('programas','Nombre', nom, 'centro', des)
        api = requests.put(url+tab+"/"+nom+"/"+tel+"/"+des+"/"+id)
        if api.status_code == 200:         
                mensaje = f'El programa fue actualizado.'
                flash(mensaje)
        else:
            mensaje = "a ocurrido un problema, no se pudo actualizar la informacion del programa."
            flash(mensaje)

    #borrar datos
    def borrar(self, tab, dat, id):
        url = "http://127.0.0.1:8000/const/delete/"
        api = requests.delete(url+tab+"/"+dat+"/"+id)
        
        if api.status_code == 200:
            mensaje = f'El centro fue eliminado correctamente.'
            flash(mensaje)
        else:
            mensaje = "a ocurrido un problema, no se pudo eliminar el centro."
            flash(mensaje)




 