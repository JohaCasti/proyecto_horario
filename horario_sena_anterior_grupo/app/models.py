from app import db, login 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

#Modelos

class Administrador(db.Model, UserMixin):
    __tablename__ = "Administrador"
    id_administrador = db.Column(db.Integer, primary_key=True)
    Nombres_admin = db.Column(db.String(40), nullable=False)
    Apellidos_admin = db.Column(db.String(40), nullable=False)
    Tel_admin = db.Column(db.String(12), nullable=False)
    Tipo_admin = db.Column(db.String(15), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def get_id(self):
        return str(self.id_administrador)

@login.user_loader
def load_user(id):
    return Administrador.query.get(int(id))

class Regional(db.Model):
    __tablename__ = "Regional"
    id_Regional = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.Text, nullable=False)
    Departamento = db.Column(db.Text, nullable=False)
    Id_Administrador = db.Column(db.Integer, db.ForeignKey('Administrador.id_administrador'), nullable=True)
    administrador = db.relationship('Administrador', backref='regionales')

class Centro(db.Model):
    __tablename__ = "Centro"
    id_Centro = db.Column(db.Integer, primary_key=True)
    Id_Regional = db.Column(db.Integer, db.ForeignKey('Regional.id_Regional'), nullable=False)
    Nombre = db.Column(db.Text, nullable=False)
    Areas = db.Column(db.Text, nullable=False)
    Descripcion = db.Column(db.Text, nullable=False)
    regional = db.relationship('Regional', backref='centros')

class Instructor(db.Model):
    __tablename__ = "Instructor"
    id_instructor = db.Column(db.Integer, primary_key=True)
    Id_Centro = db.Column(db.Integer, db.ForeignKey('Centro.id_Centro'), nullable=False)
    Nombre = db.Column(db.Text, nullable=False)
    Apellido = db.Column(db.Text, nullable=False)
    Num_identificacion = db.Column(db.String(12), nullable=False)
    Tipo_Contrato = db.Column(db.String(20), nullable=False)
    Horas_Semanales = db.Column(db.Integer, nullable=False)
    Horas_Diarias = db.Column(db.Integer, nullable=False)
    centro = db.relationship('Centro', backref='instructores')

class Ambiente(db.Model):
    __tablename__ = "Ambiente"
    id_Ambiente = db.Column(db.Integer, primary_key=True)
    Id_Centro = db.Column(db.Integer, db.ForeignKey('Centro.id_Centro'), nullable=False)
    Numero = db.Column(db.Text, nullable=False)
    Disponibilidad = db.Column(db.Text, nullable=False)
    Tipo = db.Column(db.Text, nullable=False)
    Horas_Disp = db.Column(db.Integer, nullable=False)
    Horas_Ocup = db.Column(db.Integer, nullable=False)
    centro = db.relationship('Centro', backref='ambientes')

class Coordinacion(db.Model):
    __tablename__ = "Coordinacion"
    id_Coordinacion = db.Column(db.Integer, primary_key=True)
    Id_Centro = db.Column(db.Integer, db.ForeignKey('Centro.id_Centro'), nullable=False)
    Nombre_coordinacion = db.Column(db.Text, nullable=False)
    centro = db.relationship('Centro', backref='coordinaciones')

class Programa(db.Model):
    __tablename__ = "Programa"
    id_Programa = db.Column(db.Integer, primary_key=True)
    Id_Coordinacion = db.Column(db.Integer, db.ForeignKey('Coordinacion.id_Coordinacion'), nullable=False)
    Nombre_progr = db.Column(db.String(50), nullable=False)
    coordinacion = db.relationship('Coordinacion', backref='programas')

class Ficha(db.Model):
    __tablename__ = "Ficha"
    id_Ficha = db.Column(db.Integer, primary_key=True)
    Id_Programa = db.Column(db.Integer, db.ForeignKey('Programa.id_Programa'), nullable=False)
    Numero_Ficha = db.Column(db.Integer, nullable=False)
    programa = db.relationship('Programa', backref='fichas')

class Tematica(db.Model):
    __tablename__ = "Tematica"
    id_Tematica = db.Column(db.Integer, primary_key=True)
    Id_Programa = db.Column(db.Integer, db.ForeignKey('Programa.id_Programa'), nullable=False)
    Nombre = db.Column(db.Text, nullable=False)
    Tipo_tematica = db.Column(db.String(50), nullable=False)
    Duracion_Semana = db.Column(db.Integer, nullable=False)
    Descripcion = db.Column(db.Text, nullable=False)
    programa = db.relationship('Programa', backref='tematicas')

class Resultado_de_aprendizaje(db.Model):
    __tablename__ = "Resultado_de_aprendizaje"
    id_Resul_apr = db.Column(db.Integer, primary_key=True)
    Id_Tematica = db.Column(db.Integer, db.ForeignKey('Tematica.id_Tematica'), nullable=False)
    Nombre = db.Column(db.Text, nullable=False)
    Tipo = db.Column(db.String(20), nullable=False)
    Estado = db.Column(db.Text, nullable=False)
    tematica = db.relationship('Tematica', backref='resultados_de_aprendizaje')

class Horario(db.Model):
    __tablename__ = "Horario"
    id_Horario = db.Column(db.Integer, primary_key=True)
    Nombre_iden = db.Column(db.String(30), nullable=False)
    NumeroDias = db.Column(db.Integer, nullable=False)
    NumeroBloquesxDia = db.Column(db.Integer, nullable=False)
    Id_Programa = db.Column(db.Integer, db.ForeignKey('Programa.id_Programa'), nullable=False)
    programa = db.relationship('Programa', backref='horarios')

class Bloque(db.Model):
    __tablename__ = "Bloque"
    id_Bloque = db.Column(db.Integer, primary_key=True)
    Id_Tematica = db.Column(db.Integer, db.ForeignKey('Tematica.id_Tematica'), nullable=True)
    Id_Ficha = db.Column(db.Integer, db.ForeignKey('Ficha.id_Ficha'), nullable=True)
    Id_Ambiente = db.Column(db.Integer, db.ForeignKey('Ambiente.id_Ambiente'), nullable=True)
    Id_Instructor = db.Column(db.Integer, db.ForeignKey('Instructor.id_instructor'), nullable=True)
    Id_Horario = db.Column(db.Integer, db.ForeignKey('Horario.id_Horario'), nullable=False)
    Dia = db.Column(db.Integer, nullable=False)
    Hora = db.Column(db.Integer, nullable=False)
    horario = db.relationship('Horario', backref='bloques')
    tematica = db.relationship('Tematica', backref='bloques')
    ficha = db.relationship('Ficha', backref='bloques')
    ambiente = db.relationship('Ambiente', backref='bloques')
    instructor = db.relationship('Instructor', backref='bloques')
