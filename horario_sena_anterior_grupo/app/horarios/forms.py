from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import InputRequired

class HorarioForm():
    Nombre_iden = StringField("Ingrese el nombre del horario ", validators=[InputRequired('Nombres requeridos')]) 
    NumeroDias= IntegerField("Ingrese los numeros de los dias ", validators=[InputRequired('numeros dias requeridos')]) 
    NumeroBloquesxDia = IntegerField("Ingrese el numero de bloques", validators=[InputRequired('numero de dias por bloque requeridos')])
    Id_Programa = SelectField("Seleccione el Programa:", choices=[(1, 'Option 1')], validators=[InputRequired('Programa requerido')])
class NewHorarioForm(FlaskForm):
    Nombre_iden = StringField("Ingrese el nombre del horario", validators=[InputRequired('Nombre requerido')]) 
    NumeroDias= StringField("Ingrese numeros de los dias a mostrar ", validators=[InputRequired('numeros de dias requeridos')]) 
    NumeroBloquesxDia= IntegerField("Ingrese el numero de bloques", validators=[InputRequired('numero de bloques requeridos')])
    Id_Programa = SelectField("Seleccione el Programa:", choices=[(1, 'Option 1')], validators=[InputRequired('Programa requerido')])
    submit = SubmitField("Guardar")
    
class EditHorarioForm(FlaskForm, HorarioForm):
        submit = SubmitField("Actualizar")