from models import *
from flask import jsonify, render_template

recetas = []

# receta test
receta1 = Receta(
    nombre='Enchiladas', 
    dificultad='Normal',
    tiempo='1hr',
    calorias='Descripción del artículo',
    costo=500,
    calificacion=3,
)
receta2 = Receta(
    nombre='Chilaquiles', 
    dificultad='Fácil',
    tiempo='30min',
    calorias='Descripción del artículo',
    costo=300,
    calificacion=4,
)
receta3 = Receta(
    nombre='Tacos', 
    dificultad='Difícil',
    tiempo='2hr',
    calorias='Descripción del artículo',
    costo=400,
    calificacion=5,
)
receta4 = Receta(
    nombre='Pasta', 
    dificultad='Normal',
    tiempo='25min',
    calorias='Descripción del artículo',
    costo=100,
    calificacion=2,
)
recetas.append(receta1)
recetas.append(receta2)
recetas.append(receta3)
recetas.append(receta4)


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

def ver_receta(id):
    """
    De ruta /ver_receta/<id> para ver los atributos de una receta en 
    específico

    Te paso un objeto llamado receta con los siguientes atributos:
        - nombre
        - tiempo
        - costo
        - dificultad
        - calificacion
        - calorias
        - ingredientes (lista)
        - pasos (lista)

    """
    return render_template('big_card.html', recetas=receta1)
