from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import InputRequired

class ProgramaForm():
    Nombre_progr = StringField("Ingrese el nombre de la coordinación ", validators=[InputRequired('coordinación requerida')]) 
    Id_Coordinacion = SelectField("Seleccione la Coordinación:", choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')], validators=[InputRequired('Coordinacion requerida')])

class NewProgramaForm(FlaskForm):
    Nombre_progr = StringField("Ingrese el nombre de la coordinación ", 
                                      validators=[InputRequired('coordinación requerida')]) 
    Id_Coordinacion = SelectField("Seleccione la Coordionación:", choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')], validators=[InputRequired('Coordinacion requerida')])
    submit = SubmitField("Guardar")
    
class EditProgramaForm(FlaskForm,
                          ProgramaForm):
        submit = SubmitField("Actualizar")