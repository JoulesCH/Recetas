from models import *
from flask import jsonify, render_template

recetas = []

# receta test
receta1 = Receta(
    nombre='Enchiladas', 
    dificultad=5,
    tiempo=120,
    calorias=80,
    costo=500,
    calificacion=3,
)
receta2 = Receta(
    nombre='Chilaquiles', 
    dificultad=5,
    tiempo=120,
    calorias=80,
    costo=500,
    calificacion=3,
)
recetas.append(receta1)
recetas.append(receta2)


def index():
    """
    De ruta / se mostrarán todas las recetas

    Te paso una lista llamada recetas con los siguientes atributos:
        - nombre
        - tiempo
        - costo
        - dificultad
        - calificacion
        - calorias
        - ingredientes (lista)
        - pasos (lista)
    Cada receta debe llevar un enlace para verla a detalle, incluídos los pasos y los ingredientes a detalle
    """
    return render_template('index.html', recetas=recetas)


def crear_receta():
    """
    De ruta /crear se hará un formulario para crear una receta
        - nombre
        - tiempo
        - costo
        - dificultad
        - calificacion
        - calorias
        - ingredientes (lista)
        - pasos (lista)
    """
    return render_template('crear_receta.html')