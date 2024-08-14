from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import InputRequired


class CentroForm():
    Nombre = StringField("Ingrese el nombre del centro: ", validators=[InputRequired('Nombre requerido')]) 
    Areas = StringField("Ingrese el area de estudios del centro: ", validators=[InputRequired('Area requerido')]) 
    Descripcion = StringField("Ingrese una descripción breve del centro: ", validators=[InputRequired('Ingresa una descripción')]) 
    Id_Regional = SelectField("Seleccione el centro:", choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')], validators=[InputRequired('Centro requerido')])

class NewCentroForm(FlaskForm):
    Nombre = StringField("Ingrese el nombre del centro: ", validators=[InputRequired('Nombre requerido')]) 
    Areas = StringField("Ingrese el area de estudios del centro: ", validators=[InputRequired('Area requerido')]) 
    Descripcion = StringField("Ingrese una descripción breve del centro: ", validators=[InputRequired('Ingresa una descripción')]) 
    Id_Regional = SelectField("Seleccione la Regional:", choices=[(1, "1")], validators=[InputRequired('Rgeional requerido')])
    submit = SubmitField("Guardar")
    
class EditCentroForm(FlaskForm,
                          CentroForm):
        submit = SubmitField("Actualizar")