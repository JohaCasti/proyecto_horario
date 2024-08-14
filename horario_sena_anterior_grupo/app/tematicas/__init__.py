from flask import Blueprint

tematicas = Blueprint('tematicas',__name__,
                    url_prefix = '/tematicas',
                    template_folder = 'templates')

from . import routes