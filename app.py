from flask import Flask, render_template,request,session
from werkzeug.utils import redirect
import json
import os

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def principal():
    error = None
    if request.method == 'POST':
        #realizamos la lectura del archivo para comprobar la existencia del usuario
        diccionarioUsuariosArchivo = None
        
        #abrimos el archivo usuarios.json
        with open('static/usuarios/usuarios.json') as file:
            #comprobamos sis está vacio el diccionario
            if os.stat('static/usuarios/usuarios.json').st_size == 0:
                diccionarioUsuariosArchivo = dict()
            else:
                data = json.load(file)
                diccionarioUsuariosArchivo = data
        
        #verificamos si el usuario está registrado
        if(request.form['usuario'] in diccionarioUsuariosArchivo):
            
            #Verificamos la contraseña del usuario
            if(request.form['password'] == diccionarioUsuariosArchivo[request.form['usuario']][1]):
                
                user = diccionarioUsuariosArchivo[request.form['usuario']][1]
                
                #damos la session al usuario
                session['usuario'] = user
                session['correo'] = request.form['usuario']
                session['admin'] = diccionarioUsuariosArchivo[request.form['usuario']][5]
                
                return redirect('/')
            else: #password incorrecto
                return render_template('principal.html',error='Password incorrecto')
        else:   #Correo incorrecto
            return render_template('principal.html',error='Email incorrecto')
    else:   #regresamos a la pagina principal
        return render_template('principal.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/internacional')
def internacional():
    return render_template('internacional.html')

@app.route('/gourmet')
def gourmet():
    return render_template('gourmet.html')

@app.route('/especial')
def especial():
    return render_template('especial.html')

@app.route('/mexicana')
def mexicana():
    return render_template('mexicana.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/registro',methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        #Se registra el usuario
        
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['email']
        #variable que mandaremos a escribir en el archivo
        diccionarioUsuariosArchivo = None
        
        #Metemos al usuario a un diccionario
        #Correo : Constrasena, nombre, apellido, carrito, pedidos, admin
        diccionarioUsuario = {correo : [request.form['password'], nombre, apellido, None, None, False]}
        
        #abrimos el archivo para meter los datos al diccionario
        with open('static/usuarios/usuarios.json') as file:
            #comprobamos sis está vacio el diccionario
            if os.stat('static/usuarios/usuarios.json').st_size == 0:
                diccionarioUsuariosArchivo = dict()
            else:
                data = json.load(file)
                diccionarioUsuariosArchivo = data
                
        #comprobamos si existe el usuario en el archivo
        if correo in diccionarioUsuariosArchivo:
            #Se debera de mostrar un cuadro emergente mencionando el error
            print("Porfa, alguien haga esto d:")
        else:   #se realizará la actualizacion del archivo
            actualizarArchivo(diccionarioUsuario,diccionarioUsuariosArchivo)
            
        #se mostrara un cuadro diciendo que ya se registro
        
        #mandamos al usuario a la pagina principal
        return redirect('/')
    return render_template('registro.html')

@app.route('/italiana')
def italiana():
    return render_template('italiana.html')

@app.route('/argentina')
def argentina():
    return render_template('argentina.html')

@app.route('/china')
def china():
    return render_template('china.html')

@app.route('/cocina')
def cocina():
    return render_template('cocina.html')

@app.route('/conservas')
def conservas():
    return render_template('conservas.html')

@app.route('/japonesa')
def japonesa():
    return render_template('japonesa.html')

@app.route('/tailandesa')
def tailandesa():
    return render_template('tailandesa.html')

@app.route('/panaderia')
def panaderia():
    return render_template('panaderia.html')

@app.route('/reposteria')
def reposteria():
    return render_template('reposteria.html')

@app.route('/taquiza')
def taquiza():
    return render_template('taquiza.html')

@app.route('/navidad')
def navidad():
    return render_template('navidad.html')

@app.route('/parrilladas')
def parilladas():
    return render_template('parrilladas.html')

if __name__ == '__main__':
    app.run(debug=True)


def actualizarArchivo(diccionarioUsuario,diccionarioArchivo):
    #juntamos los diccionarios
    diccionarioArchivo.update(diccionarioUsuario)
            
    #metemos los datos al json
    with open('static/usuarios/usuarios.json',"w") as outfile:  #abrimos el archivo e indicamos que vamos a escribir en él
        json.dump(diccionarioArchivo,outfile)
        
