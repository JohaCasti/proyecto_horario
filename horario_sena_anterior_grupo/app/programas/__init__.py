from flask import Blueprint, render_template


programas = Blueprint('programas',__name__,
                    url_prefix = '/programas',
                    template_folder = 'templates')

from . import routes