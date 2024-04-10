from flask import Flask,render_template,url_for,request
from flask_wtf import FlaskForm #--> configura una clave para formularios
from wtforms import StringField ,SubmitField

import datetime
app= Flask(__name__)
app.config['SECRET_KEY']='11062003WEB1' #CLAVE SECRETA
class Backend:

    def __init__(self):
         pass
        

    @app.route('/inicio/<nombre>/<apellido>/<int:cedula>') #--> ruta de las paginas web
    def Inicio(nombre,apellido,cedula):

        datos={'nombre':nombre , 'Apellido':apellido , 'Cedula':cedula}
        if (nombre ==None and apellido == apellido and cedula==None ):
            return render_template('Inicio.html')
        else:
            return render_template('Inicio.html',datos=datos)
        
        
    @app.route('/cambiarContrasena/<usuario>')
    def CambioContraseña (usuario):
        return render_template('CambioContraseña.html' , usuario=usuario) #--> llamar a el html 
    
    
    @app.route('/registro/<int:id>', methods = ['POST'])
    def registroUsuario(id):
        nombre= request.form['name']
        apellido= request.form['lastname']
        identificacion= request.form['identificacion']
        Telefono=int(Telefono= request.form['Telefono'])
        
        print(nombre,apellido,identificacion,Telefono)
        
        if request.method == 'POST':
       
            return render_template('formulario_registro.html', ide=id) 
        # else:
       
        #  return 
    
           
        
if __name__=='__main__':
     Backend1=Backend()
     print(Backend.registroUsuario(11062003))    


