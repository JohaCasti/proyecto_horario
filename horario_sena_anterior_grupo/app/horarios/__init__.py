from flask import Blueprint


horarios = Blueprint('horarios',__name__,
                    url_prefix = '/horarios',
                    template_folder = 'templates')

from . import routes