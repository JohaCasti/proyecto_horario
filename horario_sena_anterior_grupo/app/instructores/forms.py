from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import InputRequired

class InstructorForm():
    Nombre = StringField("Ingrese los nombres ", validators=[InputRequired('Nombres requeridos')]) 
    Apellido= StringField("Ingrese los apellidos ", validators=[InputRequired('Apellidos requeridos')]) 
    Num_identificacion= IntegerField("Ingrese el número de identificación", validators=[InputRequired('Número requerido')]) 
    Tipo_Contrato= SelectField("Eliga su tipo de contrato", choices=[("De planta", 'De planta'), ('Contratista', 'Contratista'), ('Otro', 'Otro')],  validators=[InputRequired('Contrato requerido')])
    Horas_Semanales = IntegerField("Ingrese las Horas Semanales ", validators=[InputRequired('Horas requeridas')]) 
    Horas_Diarias = IntegerField("Ingrese las Horas Diarias ", validators=[InputRequired('Horas requeridas')]) 
    Id_Centro = SelectField("Seleccione el centro:", choices=[(1, 'Centro de gestion de mercados'), (2, 'Option 2'), (3, 'Option 3')], validators=[InputRequired('Centro requerido')])

class NewInstructorForm(FlaskForm):
    Nombre = StringField("Ingrese los nombres ", 
                         validators=[InputRequired('Nombres requeridos')]) 
    Apellido= StringField("Ingrese los apellidos ", 
                          validators=[InputRequired('Apellidos requeridos')]) 
    Num_identificacion= IntegerField("Ingrese el número de identificación", 
                                     validators=[InputRequired('Número requerido')]) 
    Tipo_Contrato= SelectField("Eliga su tipo de contrato", choices=[("De planta", 'De planta'), ('Contratista', 'Contratista'), ('Otro', 'Otro')], 
                               validators=[InputRequired('Contrato requerido')])
    Horas_Semanales = IntegerField("Ingrese las Horas Semanales ", 
                                   validators=[InputRequired('Horas requeridas')]) 
    Horas_Diarias = IntegerField("Ingrese las Horas Diarias Maximas a Trabajar", 
                                 validators=[InputRequired('Horas requeridas')]) 
    Id_Centro = SelectField("Seleccione el centro:", choices=[(1, 'Centro de gestion de mercados'), (2, 'Option 2'), (3, 'Option 3')], 
                            validators=[InputRequired('Centro requerido')])
    submit = SubmitField("Guardar")
    
class EditInstructorForm(FlaskForm,
                          InstructorForm):
        submit = SubmitField("Actualizar")