#importar librerias de Flask y tkinter
from tkinter import SW
from flask import Flask, redirect, request,render_template, url_for

#Iniciar variable de aplicacion 
app= Flask(__name__)

#Definición de arreglo para ingresar los datos
tareasPendientes = []

#Definición de ruta
@app.route('/' )
#Función inicio que llamara a nuestra página inicio
def inicio():
    return render_template('inicio.html')

#Definición de ruta
@app.route('/' )
#Función inicio que llamara a nuestra página preguntas
def preguntas():
    return render_template('preguntas.html')

#Definición de ruta
@app.route('/' )
#Función inicio que llamara a nuestra página comestibles
def inicio():
    return render_template('imp_comestible.html')

#Definición de ruta
@app.route('/' )
#Función inicio que llamara a nuestra página electronico
def inicio():
    return render_template('imp_electronico.html')

#Definición de ruta
@app.route('/' )
#Función inicio que llamara a nuestra página quimico
def inicio():
    return render_template('imp_quimico.html')

#Definición de ruta
@app.route('/' )
#Función inicio que llamara a nuestra página agroindustrial
def inicio():
    return render_template('imp_agroindustrial.html')

#Definición de ruta
@app.route('/' )
#Función inicio que llamara a nuestra página informacion
def inicio():
    return render_template('informacion.html')

#Definición de ruta
@app.route('/' )
#Función inicio que llamara a nuestra página transparencia
def inicio():
    return render_template('transparencia.html')

#Definición de ruta
@app.route('/' )
#Función inicio que llamara a nuestra página inicio
def inicio():
    return render_template('inicio.html')

#Definición de ruta
@app.route('/' )
#Función inicio que llamara a nuestra página inicio
def inicio():
    return render_template('inicio.html')


# #segundo controlador el cuál almacenara los elementos que ingresemos por el formulario HTML
# @app.route('/enviar',  methods=['GET','POST'])
# #Función enviar la cuál podrá almacenar los datos ingresados por medio del formulario dentro de nuestro arreglo
# def enviar():
#     if(request.method == "POST"):
#         tareas = request.form['tarea']
#         correos = request.form['correo']
#         prioridades = request.form['prioridad']
#         tareasPendientes.append({'tarea': tareas, 'correo': correos, 'prioridad': prioridades })
#         return redirect(url_for('principal'))

# #Tercer controlador el cuál borrara la lista de tareas
# @app.route('/borrar', methods=["GET","POST"])
# #Función borrar la cuál limpiara todos los elementos que se encuentren almacenados dentro de nuestro arreglo
# def borrar():
#     if(request.method == "POST"):
#         tareasPendientes.clear()
#         return redirect(url_for('principal'))

# main del programa 
if __name__ == '__main__':
    #debug = true, para reiniciar automaticamente el servidor, tiempo de desarrollo 
    app.run(debug=True)