from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    username=StringField(label="Nombre de usuario",
                        validators=[InputRequired("Nombre de usuario requerido")]
                        )
    password = PasswordField(label="Contraseña",
                         validators=[InputRequired("Contraseña requerida"),
                                     Length(min=8, message="La contraseña debe tener al menos 8 caracteres")]
                        )
                           
    submit=SubmitField(label="Iniciar sesion", render_kw={'class': 'button-log'})