from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import InputRequired,NumberRange, Email, Length


class AdminForm(): 
    Nombres_admin = StringField("Ingrese sus nombres: ",
                                 validators=[InputRequired('Nombres requeridos')]) 
    Apellidos_admin = StringField("Ingrese sus Apellidos: ",
                                   validators=[InputRequired("Apellidos requeridos")])  
    username =  StringField("Ingrese su usuario",
                            validators=[InputRequired(message='usuario requerido')])
    Tel_admin = StringField("Ingrese su número de telefono: ",
                             validators=[InputRequired("Número requerido")])
    Tipo_admin =SelectField("Que tipo de administrador es:",
                             choices=[('Administrador', 'Administrador'), ('Coordinador', 'Coordinador')], validators=[InputRequired()])
    password = PasswordField("Ingrese la contraseña",
                             validators=[InputRequired(message='Contraseña requerida')])



class NewAdminForm(FlaskForm):

    Nombres_admin = StringField("Ingrese sus nombres: ",
                        validators=[InputRequired()]
                        )
    Apellidos_admin = StringField("Ingrese sus Apellidos: ",
                        validators=[InputRequired()]
                        )
    
    username = StringField("Ingrese el usuario: ",
                        validators=[InputRequired()]
                        )
    
    Tel_admin = StringField("Ingrese su número de telefono: ",
                        validators=[InputRequired(
                             "Número requerido"
                        )])
    
    Tipo_admin =SelectField("Que tipo de administrador es:",
                        choices=[('Administrador', 'Administrador'), ('Coordinador', 'Coordinador')],
                        validators=[InputRequired()]
                        )
    
    password = PasswordField("Ingrese la constraseña",
                          validators=[InputRequired(), Length(8)]
                        )
    code = StringField("Ingrese el codigo para registrarse", validators=[InputRequired(),Length(5)])

    submit = SubmitField("Guardar")
    

class EditAdminForm(FlaskForm,
                          AdminForm):
        submit = SubmitField("Actualizar")