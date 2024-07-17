from flask import (
    url_for, redirect, flash, session
)
from .models_db import *
from project import db
#crud
class CRUD:

    def crear_centro(self, nombre, tel, des, mensaje = None):
        datos = Centro (
            nombre, tel, des
        )
        peti = Centro.query.filter_by(Nombre = nombre).first()
        if peti == None:
            db.session.add(Centro(nombre, tel, des))
            db.session.commit()
            mensaje = f'El {self.tabla} {nombre}  fue creado exitosamente!!!'
            flash(mensaje)
            return redirect(url_for('admin.create'))
        else:
            mensaje = f'El {nombre}  ya existe'
            flash(mensaje)