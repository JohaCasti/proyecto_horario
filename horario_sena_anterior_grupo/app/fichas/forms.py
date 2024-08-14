from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import InputRequired


class FichaForm():
    Numero_Ficha = IntegerField("Ingrese el numero de la ficha: ", validators=[InputRequired('Nombre requerido')]) 
    Id_Programa = SelectField("Seleccione el Programa:", choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')], validators=[InputRequired('ficha requerido')])

class NewFichaForm(FlaskForm):
    Numero_Ficha = IntegerField("Ingrese el nombre del ficha: ", validators=[InputRequired('Nombre requerido')]) 
    Id_Programa = SelectField("Seleccione el Programa:", choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')], validators=[InputRequired('ficha requerido')])
    submit = SubmitField("Guardar")
    
class EditFichaForm(FlaskForm, FichaForm):
        submit = SubmitField("Actualizar")