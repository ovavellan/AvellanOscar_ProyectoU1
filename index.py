#importar librerias de Flask y tkinter
from tkinter import SW
from flask import Flask, redirect, request,render_template, url_for

#Iniciar variable de aplicacion 
app= Flask(__name__, template_folder='templates')

#Definición de arreglo para ingresar los datos
listaComestibles = []
listaElectronico = []
listaQuimico = []
listaAgroindustrial = []
listaProveedores = []

#Definición de ruta
@app.route('/' )
#Función inicio que llamara a nuestra página inicio
def inicio():
    return render_template('inicio.html')

#Definición de ruta
@app.route('/preguntas' )
#Función inicio que llamara a nuestra página preguntas
def preguntas():
    return render_template('preguntas.html')

#Definición de ruta
@app.route('/comestibles')
#Función inicio que llamara a nuestra página comestibles
def comestibles():
    return render_template('imp_comestible.html', lcomestibles = listaComestibles)
#controlador para ingresar datos en comestibles
@app.route('/ingresar_comestibles', methods=['GET','POST'])
def ingresar_comestibles():
    if(request.method == "POST"):
        productos_cm = request.form['producto_cm']
        precios_cm = request.form['precio_cm']
        cantidades_cm = request.form['cantidad_cm']
        listaComestibles.append({'producto_cm': productos_cm, 'precio_cm': precios_cm, 'cantidad_cm': cantidades_cm })
        return redirect(url_for('comestibles'))
#Controlador para borrar los productos de la lista
@app.route('/borrar_comestibles', methods=["GET","POST"])
#Función borrar la cuál limpiara todos los elementos que se encuentren almacenados dentro de nuestro arreglo
def borrar_comestible():
    if(request.method == "POST"):
        listaComestibles.clear()
        return redirect(url_for('comestibles'))



#Definición de ruta
@app.route('/electronico' )
#Función inicio que llamara a nuestra página electronico
def electronico():
    return render_template('imp_electronico.html', lelectronico = listaElectronico)
#controlador para ingresar datos en comestibles
@app.route('/ingresar_electronico', methods=['GET','POST'])
def ingresar_electronico():
    if(request.method == "POST"):
        productos_el = request.form['producto_el']
        precios_el = request.form['precio_el']
        cantidades_el = request.form['cantidad_el']
        listaElectronico.append({'producto_el': productos_el, 'precio_el': precios_el, 'cantidad_el': cantidades_el })
        return redirect(url_for('electronico_el'))
#Controlador para borrar los productos de la lista
@app.route('/borrar_electronico', methods=["GET","POST"])
#Función borrar la cuál limpiara todos los elementos que se encuentren almacenados dentro de nuestro arreglo
def borrar_electronico():
    if(request.method == "POST"):
        listaElectronico.clear()
        return redirect(url_for('electronico'))



#Definición de ruta
@app.route('/quimico' )
#Función inicio que llamara a nuestra página quimico
def quimico():
    return render_template('imp_quimico.html', lquimico = listaQuimico)
#controlador para ingresar datos en comestibles
@app.route('/ingresar_quimico', methods=['GET','POST'])
def ingresar_quimicos():
    if(request.method == "POST"):
        productos_qm = request.form['producto_qm']
        precios_qm = request.form['precio_qm']
        cantidades_qm = request.form['cantidad_qm']
        listaQuimico.append({'producto_qm': productos_qm, 'precio_qm': precios_qm, 'cantidad_qm': cantidades_qm })
        return redirect(url_for('quimico'))
#Controlador para borrar los productos de la lista
@app.route('/borrar_qumico', methods=["GET","POST"])
#Función borrar la cuál limpiara todos los elementos que se encuentren almacenados dentro de nuestro arreglo
def borrar_quimico():
    if(request.method == "POST"):
        listaQuimico.clear()
        return redirect(url_for('quimico'))



#Definición de ruta
@app.route('/agroindustrial' )
#Función inicio que llamara a nuestra página agroindustrial
def agroindustrial():
    return render_template('imp_agroindustrial.html', lagroindustrial = listaAgroindustrial)
#controlador para ingresar datos en comestibles
@app.route('/ingresar_agroindustrial', methods=['GET','POST'])
def ingresar_agroindustrial():
    if(request.method == "POST"):
        productos_ag = request.form['producto_ag']
        precios_ag = request.form['precio_ag']
        cantidades_ag = request.form['cantidad_ag']
        listaAgroindustrial.append({'producto_ag': productos_ag, 'precio_ag': precios_ag, 'cantidad_ag': cantidades_ag })
        return redirect(url_for('agroindustrial'))
#Controlador para borrar los productos de la lista
@app.route('/borrar_agroindustrial', methods=["GET","POST"])
#Función borrar la cuál limpiara todos los elementos que se encuentren almacenados dentro de nuestro arreglo
def borrar_agroindustrial():
    if(request.method == "POST"):
        listaAgroindustrial.clear()
        return redirect(url_for('agroindustrial'))



#Definición de ruta
@app.route('/proveedores' )
#Función inicio que llamara a nuestra página proveedores
def proveedores():
    return render_template('proveedores.html', lproveedor = listaProveedores)

#controlador para ingresar datos en comestibles
@app.route('/ingresar_proveedor', methods=['GET','POST'])
def ingresar_proveedor():
    if(request.method == "POST"):
        productos_pv = request.form['producto_pv']
        precios_pv = request.form['precio_pv']
        cantidades_pv = request.form['cantidad_pv']
        listaProveedores.append({'producto_pv': productos_pv, 'precio_pv': precios_pv, 'cantidad_pv': cantidades_pv })
        return redirect(url_for('proveedores'))
#Controlador para borrar los productos de la lista
@app.route('/borrar_proveedor', methods=["GET","POST"])
#Función borrar la cuál limpiara todos los elementos que se encuentren almacenados dentro de nuestro arreglo
def borrar_proveedor():
    if(request.method == "POST"):
        listaProveedores.clear()
        return redirect(url_for('proveedores'))



#Definición de ruta
@app.route('/informacion' )
#Función inicio que llamara a nuestra página informacion
def informacion():
    return render_template('informacion.html')

#Definición de ruta
@app.route('/transparencia' )
#Función inicio que llamara a nuestra página transparencia
def transparencia():
    return render_template('transparencia.html')

#Definición de ruta
@app.route('/contacto' )
#Función inicio que llamara a nuestra página contaco
def contacto():
    return render_template('contacto.html')

# main del programa 
if __name__ == '__main__':
    #debug = true, para reiniciar automaticamente el servidor, tiempo de desarrollo 
    app.run(debug=True)