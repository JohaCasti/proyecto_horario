from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import InputRequired,NumberRange, Email, Length

class RegionForm():
    Nombre = StringField("Ingrese el nombre de la regional: ", validators=[InputRequired('Nombre requerido')]) 
    Departamento = StringField("Ingrese el departamento donde se encuentra la regional: ", validators=[InputRequired('Departamento requerido')]) 

class NewRegionForm(FlaskForm):
    Nombre = StringField("Ingrese el nombre de la regional: ", 
                                validators=[InputRequired('Nombre requerido')]) 
    Departamento = StringField("Ingrese el departamento donde se encuentra la regional: ",
                                 validators=[InputRequired('Departamento requerido')]) 
    submit = SubmitField("Guardar")
    
class EditRegionForm(FlaskForm,
                          RegionForm):
        submit = SubmitField("Actualizar")