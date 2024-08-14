from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import InputRequired,NumberRange, Email, Length

class TematicaForm():
    Nombre = StringField("Ingrese el nombre de la regional: ", validators=[InputRequired('Nombre requerido')]) 
    Tipo_tematica = SelectField("Seleccione el tipo de Tematica:", choices=[(1, 'Unica'), (2, 'Transversal')], validators=[InputRequired('Programa requerido')]) 
    Duracion_Semana =  IntegerField("Ingrese las horas del programa semanalmente ", validators=[InputRequired('Horas Requeridas')])
    Descripcion = StringField("Ingrese una breve descripción: ", validators=[InputRequired('Descripcion requerida')]) 
    Id_Programa = SelectField("Seleccione el Programa:", choices=[(1, 'Option 1')], validators=[InputRequired('Programa requerido')]) 

class NewTematicaForm(FlaskForm):
    Nombre = StringField("Ingrese el nombre de la regional: ", validators=[InputRequired('Nombre requerido')]) 
    Tipo_tematica = SelectField("Seleccione el tipo de Tematica:", choices=[(1, 'Unica'), (2, 'Transversal')], validators=[InputRequired('Programa requerido')]) 
    Duracion_Semana =  IntegerField("Ingrese las horas del programa semanalmente ", validators=[InputRequired('Horas Requeridas')])
    Descripcion = StringField("Ingrese una breve descripción: ", validators=[InputRequired('Descripcion requerida')]) 
    Id_Programa = SelectField("Seleccione el Programa:", choices=[(1, 'Option 1')], validators=[InputRequired('Programa requerido')]) 
    submit = SubmitField("Guardar")
    
class EditTematicaForm(FlaskForm, TematicaForm):
        submit = SubmitField("Actualizar")
