from flask import Flask, render_template, request, redirect, url_for
from app.sistema_horarios import sistema_horarios
import app  # Asegúrate de importar tu base de datos desde tu aplicación

# Inicializa el horario vacío
schedule = {day: {hour: {"id_Bloque": None, "ficha": "", "ambiente": "", "tematica": "", "instructor": ""} for hour in range(7, 19)} for day in ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']}

@sistema_horarios.route('/b/<int:Id_Horario>')
def horarios_view(Id_Horario):
    horarios = app.models.Horario.query.get(Id_Horario)
    ficha = app.models.Ficha.query.all()
    ambiente = app.models.Ambiente.query.all()
    instructores = app.models.Instructor.query.all()
    tematica = app.models.Tematica.query.all()
    
    # Rellena el horario con datos de la base de datos
    bloques = app.models.Bloque.query.filter_by(Id_Horario=Id_Horario).all()
    for bloque in bloques:
        day = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'][bloque.Dia - 1]
        hour = bloque.Hora
        schedule[day][hour] = {
            "id_Bloque": bloque.id_Bloque,
            "ficha": bloque.ficha.Numero_Ficha if bloque.ficha else "",
            "ambiente": bloque.ambiente.Numero if bloque.ambiente else "",
            "tematica": bloque.tematica.Nombre if bloque.tematica else "",
            "instructor": bloque.instructor.Nombre if bloque.instructor else ""
        }
    return render_template('schedule.html', schedule=schedule, instructores=instructores, ficha=ficha, ambiente=ambiente, tematica=tematica, horarios=horarios)

@sistema_horarios.route('/update/<int:Id_Bloque>', methods=['POST'])
def update_schedule(Id_Bloque):
    bloques = app.models.Bloque.query.get(Id_Bloque)
    try:
        day = request.form['day']
        hour = int(request.form['hour'])
        schedule[day][hour] = {
            "ficha": request.form['ficha'],
            "ambiente": request.form['ambiente'],
            "tematica": request.form['tematica'],
            "instructor": request.form['instructor']
        }
        return redirect(url_for('bloques.horarios_view', bloques=bloques))  # Redirect to the 'index' view
    except Exception as e:
        print(f"Error: {e}")
        return f"An error occurred: {e}", 500
