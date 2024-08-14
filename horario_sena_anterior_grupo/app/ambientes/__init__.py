from flask import Blueprint, render_template

ambientes = Blueprint('ambientes',__name__,
                    url_prefix = '/ambientes',
                    template_folder = 'templates')

from . import routes