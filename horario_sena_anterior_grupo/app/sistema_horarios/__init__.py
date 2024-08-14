from flask import Blueprint, render_template

sistema_horarios = Blueprint('bloques',__name__,
                    url_prefix = '/bloques',
                    template_folder = 'templates')

from . import routes