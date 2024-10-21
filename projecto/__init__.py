from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    #configuracion del app
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'devBare'
    )
    
    from . import routes, auth
    app.register_blueprint(routes.admin)
    app.register_blueprint(auth.auth)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    
    return app