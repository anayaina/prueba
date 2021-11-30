
from flask import Flask, render_template,request,session
from werkzeug.utils import redirect
import json
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

#abrir diccionario usuarios
with open('static/usuarios/usuarios.json') as f:
    dict_usuarios = json.load(f)

#abrir diccionario productos
with open('static/Productos/productos.json') as f:
    dict_productos = json.load(f)

@app.route('/',methods=['GET','POST'])
def principal():
    return render_template('principal.html')

@app.route('/cart')
def cart():
    #declaramos el cart en session
    session["cart"] = {}
    
    #obtenemos el carrito y lo introducimos en la session solo si se ha iniciado sesion
    
    #obtenemos el correo del usuario
    correo = session["email"]
    #metemos el carrito de compras el usuario
    carrito = dict_usuarios[correo]["carrito"]
    print(carrito)
    return render_template('cart.html',cart=carrito)

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

@app.route('/mexicana',methods=['GET','POST'])
def mexicana():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('mexicana.html')
        else:
            return render_template('mexicana.html',error='Necesita iniciar sesion')
    else:
        return render_template('mexicana.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/inicio',methods=['GET','POST'])
def inicio():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        #verificamos si el usuario esta registrado
        if email in dict_usuarios:
            #verificamos la contraseña del usuario
            if dict_usuarios[email]['password'] == request.form['password']:
                session['username'] = dict_usuarios[email]['name']
                session['email'] = email
                '''
                session['nombre'] = diccionarioUsuariosArchivo[request.form['usuario']][1]
                session['user'] = request.form['usuario']''' #lo dejo xq no sé xq hay nombre y user en session
                return redirect('/')
            else:
                return render_template('inicio.html',error='Contraseña incorrecta')
        else:
            return render_template('inicio.html',error='Correo incorrecto')
    else:
        return render_template('inicio.html')

@app.route('/registro',methods=['GET','POST'])
def registro():
    error=None
    if request.method == 'POST':
        name, surname, email, password = request.form['name'], request.form['surname'], request.form['email'], request.form['password']
        if email in dict_usuarios:
            return render_template('registro.html', error='Correo ya registrado')
        dict_usuarios[email]={}
        dict_usuarios[email]['name'] = name
        dict_usuarios[email]['surname'] = surname
        dict_usuarios[email]['password'] = password
        dict_usuarios[email]['carrito'] = None
        dict_usuarios[email]['pedido'] = None
        dict_usuarios[email]['admin'] = False
        with open('static/usuarios/usuarios.json', 'w') as fp:
                json.dump(dict_usuarios, fp)
        session['username'] = name
        return redirect('/')
    return render_template('registro.html')

@app.route('/italiana',methods=['GET','POST'])
def italiana():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('italiana.html')
        else:
            return render_template('italiana.html',error='Necesita iniciar sesion')
    else:
        return render_template('italiana.html')

@app.route('/argentina',methods=['GET','POST'])
def argentina():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('argentina.html')
        else:
            return render_template('argentina.html',error='Necesita iniciar sesion')
    else:
        return render_template('argentina.html')

@app.route('/china',methods=['GET','POST'])
def china():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('china.html')
        else:
            return render_template('china.html',error='Necesita iniciar sesion')
    else:
        return render_template('china.html')

@app.route('/cocina',methods=['GET','POST'])
def cocina():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('cocina.html')
        else:
            return render_template('cocina.html',error='Necesita iniciar sesion')
    else:
        return render_template('cocina.html')

@app.route('/conservas',methods=['GET','POST'])
def conservas():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('conservas.html')
        else:
            return render_template('conservas.html',error='Necesita iniciar sesion')
    else:
        return render_template('conservas.html')

@app.route('/japonesa',methods=['GET','POST'])
def japonesa():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('japonesa.html')
        else:
            return render_template('japonesa.html',error='Necesita iniciar sesion')
    else:
        return render_template('japonesa.html')

@app.route('/tailandesa',methods=['GET','POST'])
def tailandesa():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('tailandesa.html')
        else:
            return render_template('tailandesa.html',error='Necesita iniciar sesion')
    else:
        return render_template('tailandesa.html')

@app.route('/panaderia',methods=['GET','POST'])
def panaderia():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('panaderia.html')
        else:
            return render_template('panaderia.html',error='Necesita iniciar sesion')
    else:
        return render_template('panaderia.html')

@app.route('/reposteria',methods=['GET','POST'])
def reposteria():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('reposteria.html')
        else:
            return render_template('reposteria.html',error='Necesita iniciar sesion')
    else:
        return render_template('reposteria.html')

@app.route('/taquiza',methods=['GET','POST'])
def taquiza():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('taquiza.html')
        else:
            return render_template('taquiza.html',error='Necesita iniciar sesion')
    else:
        return render_template('taquiza.html')

@app.route('/navidad',methods=['GET','POST'])
def navidad():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('navidad.html')
        else:
            return render_template('navidad.html',error='Necesita iniciar sesion')
    else:
        return render_template('navidad.html')

@app.route('/parrilladas',methods=['GET','POST'])
def parilladas():
    if request.method == 'POST':
        #Sacamos el ID del producto
        productId = request.form['comprar']
        email = session["email"]
        print(productId)
        
        #se realiza un escaneo del archivo de productos
        if email in dict_usuarios:
            #Insertamos los datos del producto en el archivo
            insertarProductoAlCarrito(dict_usuarios[email]["carrito"],productId,email)
            
            return render_template('parrilladas.html')
        else:
            return render_template('parrilladas.html',error='Necesita iniciar sesion')
    else:
        return render_template('parrilladas.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)

def insertarProductoAlCarrito(carrito,productId,email):
    #verificamos si el carrito esta vacio
    if carrito is None or len(carrito) == 0:
        carrito = dict()
        carrito[productId] = [1, dict_productos[productId]]
    else:  # si ya tiene elementos
        if productId not in dict_usuarios:  # si aun no está el producto en el carrito
            carrito[productId] = [1, dict_productos[productId]]
        else:
            carrito[productId][0] += 1

        dict_usuarios[email]["carrito"] = carrito

    #realizamos la escritura
    with open('static/usuarios/usuarios.json', 'w') as fp:
        json.dump(dict_usuarios, fp)

def actualizarArchivo(diccionarioUsuario,diccionarioArchivo):
    #juntamos los diccionarios
    diccionarioArchivo.update(diccionarioUsuario)
            
    #metemos los datos al json
    with open('static/usuarios/usuarios.json',"w") as outfile:  #abrimos el archivo e indicamos que vamos a escribir en él
        json.dump(diccionarioArchivo,outfile)
