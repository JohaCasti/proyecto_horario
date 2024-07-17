from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# creamos una extencion del sql
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    #configuracion del app
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'devBare',
        SQLALCHEMY_DATABASE_URI = "sqlite:///prueba.db"
    )

    #inicializamos conexion a la base de datos
    db.init_app(app)

    # registro de blueprint
    from . import routes, auth
    from .api import apirest
    app.register_blueprint(routes.admin)
    app.register_blueprint(auth.auth)
    app.register_blueprint(apirest.apirest)


    @app.route('/')
    def index():
        return render_template('index.html')
    

    # importa los modelos de la base de datos que falten
    with app.app_context():
        db.create_all()
    
    return app