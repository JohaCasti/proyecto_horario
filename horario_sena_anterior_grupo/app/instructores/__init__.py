from flask import Blueprint, render_template


instructores = Blueprint('instructores',__name__,
                    url_prefix = '/instructores',
                    template_folder = 'templates')

from . import routes