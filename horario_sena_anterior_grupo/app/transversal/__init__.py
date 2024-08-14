from flask import Blueprint, render_template


transversal = Blueprint('transversal',__name__,
                    url_prefix = '/transversal',
                    template_folder = 'templates')

from . import routes