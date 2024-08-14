from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import InputRequired,NumberRange, Email, Length

class AmbienteForm():
    Numero = StringField("Ingrese el numero del ambiente: ", validators=[InputRequired('Nombre requerido')]) 
    Disponibilidad = SelectField("Seleccione la disponibilidad del ambiente:", choices=[(1, 'Disponibilidad')], validators=[InputRequired('Ambiente requerido')]) 
    Tipo =  SelectField("Ingrese el tipo de ambiente ", choices=[(1, 'Sistemas')], validators=[InputRequired('Tipo Requerido')])
    Horas_Disp = IntegerField("Ingrese las horas disponibles: ", validators=[InputRequired('Horas requeridas')]) 
    Horas_Ocup = IntegerField("Ingrese las horas ocupadas:", validators=[InputRequired('Horas requeridas')]) 
    Id_Centro = SelectField("Seleccione el Programa:", choices=[(1, 'Option 1')], validators=[InputRequired('Programa requerido')])

class NewAmbienteForm(FlaskForm):
    Numero = StringField("Ingrese el numero del ambiente: ", validators=[InputRequired('Nombre requerido')]) 
    Disponibilidad = SelectField("Seleccione la disponibilidad del ambiente:", choices=[(1, 'Disponibilidad')], validators=[InputRequired('Ambiente requerido')]) 
    Tipo =  SelectField("Ingrese el tipo de ambiente ", choices=[(1, 'Sistemas')], validators=[InputRequired('Tipo Requerido')])
    Horas_Disp = IntegerField("Ingrese las horas disponibles: ", validators=[InputRequired('Horas requeridas')]) 
    Horas_Ocup = IntegerField("Ingrese las horas ocupadas:", validators=[InputRequired('Horas requeridas')])
    Id_Centro = SelectField("Seleccione el Programa:", choices=[(1, 'Option 1')], validators=[InputRequired('Programa requerido')])
    submit = SubmitField("Guardar")
    
class EditAmbienteForm(FlaskForm, AmbienteForm):
        submit = SubmitField("Actualizar")