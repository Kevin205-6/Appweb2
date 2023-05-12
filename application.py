#!/usr/bin/env python
#-*- coding: utf-8 -*-
from flask import Flask, render_template 
#Exportar las biblotecas (flask y una que le pertece a flask  "render_template"
#que permite llamar un archivo index desde una carpeta llamada templates

app = Flask(__name__) #Iniciar flask en una variable

@app.route('/') #Esto permite que cualquier archivo se llame dentro del documento desde la raiz del proyecto
def index(): #Crea un metodo para que te retorne una pagina web con html
    return render_template('index.html'); #Forma de retornar el archivo html desde la carpeta llamada templates

if __name__ == '__main__': #Si el programa se ejecuta en forma de main te inicia una aplicación de python
    app.run(debug=True)