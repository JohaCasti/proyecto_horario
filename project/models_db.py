#from project import db


   
    
#  tabla Todo
# class Todo(db.Model):
#     #Columnas
#     id = db.Column(db.Integer, primary_key = True)
#     create_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
#     title = db.Column(db.String(70), nullable = False)
#     descrip = db.Column(db.Text)
#     state = db.Column(db.Boolean, default = False)


#     def __init__(self, create_by, title, descrip, state = False):
#         self.create_by = create_by
#         self.title = title
#         self.descrip = descrip
#         self.state = state


#     def __repr__(self):
#         return f'<Todo: {self.title} >'  
    

# nombre de la tabla
# class Administrador(db.Model): 
#     #Model es una clase ya establecida de alchemy
#     id_admin = db.Column(db.Integer, primary_key = True)    
#     Nombre = db.Column(db.String(30), nullable = False)    
#     Apellido = db.Column(db.String(30), nullable = False)    
#     Telefono = db.Column(db.String(12), unique = True, nullable = False)    
#     Tipo_admin = db.Column(db.String(15), nullable = False)    
#     Username = db.Column(db.String(15), nullable = False)    
#     Password = db.Column(db.Text, nullable = False)    

#     def __init__(self, Nombre, Apellido, Telefono, Tipo_admin, Username, Password):
#         self.Nombre = Nombre
#         self.Apellido = Apellido
#         self.Telefono = Telefono
#         self.Tipo_admin = Tipo_admin
#         self.Username = Username
#         self.Password = Password

    
#     def __repr__(self):
#         return f'<User: {self.Username}>'
        

# class Centro(db.Model):
#     id_centro = db.Column(db.Integer, primary_key = True)    
#     Nombre = db.Column(db.String(80), nullable = False)       
#     Telefono = db.Column(db.String(12), nullable = False)    
#     Descrip = db.Column(db.Text, nullable = False) 

#     def __init__(self, Nombre, Telefono, Descrip):
#         self.Nombre = Nombre
#         self.Telefono = Telefono
#         self.Descrip = Descrip

#     def __repr__(self):
#         return f'<Centro: {self.Nombre}>'
    


# class Ambiente(db.Model):
#     id_ambiente = db.Column(db.Integer, primary_key = True)    
#     id_centro = db.Column(db.String(30), db.ForeignKey('centro.id_centro'), nullable = False)    
#     Salon = db.Column(db.String(4), nullable = False)    
#     Disponibilidad = db.Column(db.Boolean, default = False)          
    
#     def __init__(self, Salon, id_centro, Disponibilidad = True):
#         self.Salon = Salon
#         self.Disponibilidad = Disponibilidad
#         self.id_centro = id_centro

#     def __repr__(self):
#         return f'<Salon: {self.Salon}>'


# class Ficha(db.Model):
#     id_ficha = db.Column(db.Integer, primary_key = True)   
#     Num_ficha = db.Column(db.Integer, nullable = False)  
#     id_programa = db.Column(db.String(30), db.ForeignKey('Programa.id_programa'), nullable = False)    
#     Profesor = db.Column(db.Integer, db.ForeignKey('Instructor.id_instru'), nullable = False)  
#     Descrip = db.Column(db.Text) 

#     def __init__(self, Num_ficha, Descrip, Profesor, id_programa):
#         self.Num_ficha = Num_ficha
#         self.Descrip = Descrip
#         self.Profesor = Profesor
#         self.id_programa = id_programa

#     def __repr__(self):
#         return f'<Ficha: {self.Num_ficha}>'
    
# # #16 horas al dia
# class Horario(db.Model):
    
#     id_hora = db.Column(db.Integer, primary_key = True)
#     Hora = db.Column(db.Integer, nullable = False)
#     Tipo = db.Column(db.Integer, nullable = False)
#     Dia = db.Column(db.Integer, db.ForeignKey('Dias.id_dia'))

 
#     def __init__(self, Hora, Tipo):
#         self.Hora = Hora
#         self.Tipo = Tipo 

#     def __repr__(self):
#         return f'<Hora: {self.Tipo}>'
    

# class Dias(db.Model):
#     id_dia = db.Column(db.Integer, primary_key = True)
#     Nombre = db.Column(db.String(10), nullable = False)
#     Descrip = db.Column(db.String(30), nullable = False)

#     def __init__(self, Nombre, Descrip):
#         self.Nombre = Nombre
#         self.Descrip = Descrip

#     def __repr__(self):
#         return f'<Dia: {self.Nombre}>'
    

# class Instructor(db.Model):
#     id_instru = db.Column(db.Integer, primary_key = True)    
#     Nombre = db.Column(db.String(30), nullable = False)    
#     Apellido = db.Column(db.String(30), nullable = False)    
#     Identificacion = db.Column(db.String(15), unique = True, nullable = False)    
#     Telefono = db.Column(db.String(12), unique = True, nullable = False)       
#     Tipo_contrato = db.Column(db.String(30), nullable = False)
#     Horas_sem =  db.Column(db.Integer, nullable = False) 

#     def __init__(self, Nombre, Apellido, Identificacion, Telefono, Tipo_contrato, Horas_sem):
#         self.Nombre = Nombre
#         self.Apellido = Apellido
#         self.Identificacion = Identificacion
#         self.Telefono = Telefono
#         self.Tipo_contrato = Tipo_contrato
#         self.Horas_sem = Horas_sem


#     def __repr__(self):
#         return f'<Instructor: {self.Nombre} {self.Apellido}>'
        

# class Programa(db.Model):
#     id_programa = db.Column(db.Integer, primary_key = True)    
#     id_centro = db.Column(db.String(30), db.ForeignKey('centro.id_centro'), nullable = False)     
#     Nombre = db.Column(db.String(100), nullable = False)    
#     Descrip = db.Column(db.Text, nullable = False)    
#     Modalidad = db.Column(db.String(20), nullable = False) # diurna, todo el dia, nocturna o madrugada

#     def __init__(self, Nombre, Descrip, Modalidad, id_centro): 
#         self.Nombre= Nombre
#         self.Descrip = Descrip
#         self.Modalidad = Modalidad
#         self.id_centro = id_centro

#     def __repr__(self):
#         return f'<Programa: {self.Nombre}>'

          
    