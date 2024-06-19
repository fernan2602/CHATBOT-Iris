import nltk
from nltk.chat.util import Chat, reflections
import re
import random
import pyodbc
from flask import Flask, request, render_template , jsonify

#Importamos las clases de preguntas.py
from preguntas import Preguntas 
#Importamos respuestas de respuestas.py
from respuestas import Respuesta 
from connexion import Search
#Importar consultas
from consultapersona import ConsultaPersona
#Importar preguntas por tabla 
from preguntaspersona import PreguntasPersona
#Inicializadores de la herencia
class App:

    def Inicio(server,database):
        #Aperturamos la conexion con la base de datos 
        #Iniciar con las clases de herencia
        RUsuario = Respuesta()
        PUsuario = PreguntasPersona()
        PAll = Preguntas()
        server = 'DESKTOP-KIFUB23\SQLEXPRESS;Database=TChatBot'
        database = 'TChatBot'
        db = Search(server,database)
        #Generamos el bucle inicio para continuar con las preguntas
        continuar = True
        #Creare una biblioteca de respuestas a preguntas predeterminadas
        #Consultar el catalogo de respuestas predeterminadas
        #Generar un inicio preguntar nombre
        generar =" Como puedo ayudarte"
        #Crear un bucle consultas infinitas 
        #Creare una biblioteca de respuestas a preguntas predeterminadas
        #Creacion de un bucle para la continuidad de preguntas hasta completar lo dema:
        saludo=("Hola, soy tu asistente Personal")
        

        while (continuar == True):  
            consulta= input(""+generar+" :")
            
    
    #caso retornara la tabla tabla
    #En caso el usuario coloque una oracion dividiremos la misma en un array con el comando split()
    #Mandaremos la consulta preguntas.py para heredar la misma
            tabla = PAll.buscar_pregunta_similar(consulta.split())
        
            if tabla == "TPersona":
               consulta=input("Que le gustaria saber : ")
               columna= PUsuario.buscar_pregunta_similar(consulta.split())
               conexion=db.connect()
               results = ConsultaPersona.search_by_all(tabla,columna,conexion)
               print(results) 
               db.disconnect()
    #Ya hay un return mas especifico de la tabla y la columna para respoder
    
    


#Llamamos a la clase de buscar en la base de datos

#En caso de sea Select 
# Ejemplo de búsqueda por nombre
#Ya tenemos mas datos especificos de la tabla y columna
    
    










