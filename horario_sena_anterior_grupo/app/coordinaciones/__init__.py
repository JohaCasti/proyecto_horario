from flask import Blueprint, render_template


coordinaciones = Blueprint('coordinaciones',__name__,
                    url_prefix = '/coordinaciones',
                    template_folder = 'templates')

from . import routes