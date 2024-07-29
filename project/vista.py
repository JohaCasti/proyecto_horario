from flask import (
    Blueprint, jsonify, render_template, request, url_for, redirect, flash, session, g,
    )
from werkzeug.security import generate_password_hash, check_password_hash
import requests



vista = Blueprint('vista', __name__, url_prefix='/vista')

# Datos de ejemplo
datos_centro = {
    "CENTRO DE DISEÑO Y METROLOGÍA": {
        "fichas": ["2558697", "2458798"],
        "salones": ["702", "704"]
    },
    "CENTRO DE ELECTRICIDAD, ELECTRÓNICA Y TELECOMUNICACIONES": {
        "fichas": ["2365784", "3205489"],
        "salones": ["301", "507"]
    },
    "CENTRO DE FORMACIÓN DE TALENTO HUMANO EN SALUD": {
        "fichas": ["1234567", "2345678"],
        "salones": ["101", "102"]
    }
    
}

@vista.route('/vistad')
def vistad():
    return render_template('vista/indexadmin.html')

@vista.route('/get_fichas_salones', methods=['POST'])
def get_fichas_salones():
    centro = request.json.get('centro')
    data = datos_centro.get(centro, {"fichas": [], "salones": []})
    return jsonify(data)