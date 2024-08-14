from flask import Blueprint


administrador = Blueprint('administrador', __name__,
                            url_prefix='/administrador',
                            template_folder= 'templates')

from . import routes
