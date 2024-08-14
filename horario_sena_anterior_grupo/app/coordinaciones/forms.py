from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import InputRequired

class CoordinacionForm():
    Nombre_coordinacion = StringField("Ingrese el nombre de la coordinación ", validators=[InputRequired('Coordinación requerida')]) 
    descripcion_coordinacion = StringField("Ingrese una breve descripcion ", validators=[InputRequired('Descripción requerida')]) 
    Id_Centro = SelectField("Seleccione el centro:", choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')], validators=[InputRequired('Centro requerido')])

class NewCoordinacionForm(FlaskForm):
    Nombre_coordinacion = StringField("Ingrese el nombre de la coordinación ", 
                                      validators=[InputRequired('coordinación requerida')]) 
    descripcion_coordinacion = StringField("Ingrese una breve descripcion ", 
                                           validators=[InputRequired('Descripción requerida')]) 
    Id_Centro = SelectField("Seleccione el centro:", choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')], 
                            validators=[InputRequired('Centro requerido')])
    submit = SubmitField("Guardar")
    
class EditCoordinacionForm(FlaskForm,
                          CoordinacionForm):
        submit = SubmitField("Actualizar")