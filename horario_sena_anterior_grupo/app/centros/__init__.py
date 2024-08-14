from flask import Blueprint, render_template

centros = Blueprint('centros',__name__,
                    url_prefix = '/centros',
                    template_folder = 'templates')

from . import routes