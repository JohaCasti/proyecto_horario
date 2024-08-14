from flask import Blueprint, render_template

fichas = Blueprint('fichas',__name__,
                    url_prefix = '/fichas',
                    template_folder = 'templates')

from . import routes