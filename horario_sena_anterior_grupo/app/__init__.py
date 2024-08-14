from flask import Flask, render_template, Blueprint
from .config import Config
from app.auth import auth
from app.transversal import transversal
from app.centros import centros 
from app.regionales import regionales
from app.coordinaciones import coordinaciones
from app.programas import programas
from app.instructores import instructores
from app.administrador import administrador
from app.horarios import horarios
from app.fichas import fichas
from app.tematicas import tematicas
from app.sistema_horarios import sistema_horarios
from app.ambientes import ambientes

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

#inicializar el objeto SQLALCHEMY
db= SQLAlchemy(app)
migrate=Migrate(app, db)
login=LoginManager(app)
login.login_view="/auth/login"

#registrar modulos(blueprints)
app.register_blueprint(auth)
app.register_blueprint(centros)
app.register_blueprint(regionales)
app.register_blueprint(administrador)
app.register_blueprint(transversal)
app.register_blueprint(coordinaciones)
app.register_blueprint(programas)
app.register_blueprint(instructores)
app.register_blueprint(fichas)
app.register_blueprint(horarios)
app.register_blueprint(sistema_horarios)
app.register_blueprint(tematicas)
app.register_blueprint(ambientes)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")


from .models import *