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
                    mensaje = f'La ficha {num} registro correctamente'
                    flash(mensaje)
                else:
                    mensaje = "a ocurrido un problema, no se pudo crear la ficha.. intentalo de nuevo!"
                    flash(mensaje)
            else:
                mensaje = f'La ficha {num} ya esta registrado'
                flash(mensaje)