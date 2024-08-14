from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import InputRequired

class TransversalForm():
    Nombre_Tran = StringField("Ingrese el nombre de la transversal ", validators=[InputRequired('Transversal requerida')]) 
    Horas_Min_Sem = StringField("Ingrese las horas minimas en la semana: ", validators=[InputRequired('Horas requeridas')]) 
    Horas_Max_Sem = StringField("Ingrese las horas maximas en la semana: ", validators=[InputRequired('Horas requeridas')]) 
    Hora_Dia = StringField("Ingrese las horas en el dia", validators=[InputRequired('Horas requeridas')])

class NewTransversalForm(FlaskForm):
    Nombre_Tran = StringField("Ingrese el nombre de la transversal ", validators=[InputRequired('Transversal requerida')]) 
    Horas_Min_Sem = StringField("Ingrese las horas minimas en la semana: ", validators=[InputRequired('Horas requeridas')]) 
    Horas_Max_Sem = StringField("Ingrese las horas maximas en la semana: ", validators=[InputRequired('Horas requeridas')]) 
    Hora_Dia = StringField("Ingrese las horas en el dia", validators=[InputRequired('Horas requeridas')])
    submit = SubmitField("Guardar")
    
class EditTransversalForm(FlaskForm,
                          TransversalForm):
        submit = SubmitField("Actualizar")