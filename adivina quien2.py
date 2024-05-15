# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:04:52 2024

@author: isisa
"""






import random

# Definición de los animales y sus características
animales = {
    "Elefante": {"Grande": True, "Tiene trompa": True, "Vive en la selva": True},
    "Tigre": {"Grande": True, "Rayas": True, "Caza otros animales": True},
    "Pato": {"Vuela": True, "Nada": True, "Tiene plumas": True},
    "Cebra": {"Rayas": True, "Corre rápido": True, "Vive en la sabana": True},
    "Ballena": {"Grande": True, "Vive en el mar": True, "Tiene aletas": True},
    "León": {"Grande": True, "Melena": True, "Caza en manada": True},
    "Águila": {"Vuela": True, "Tiene pico ganchudo": True, "Vive en las montañas": True},
    "Rinoceronte": {"Grande": True, "Tiene cuerno": True, "Piel gruesa": True},
    "Murciélago": {"Vuela": True, "Nocturno": True, "Duerme cabeza abajo": True},
    "Gorila": {"Grande": True, "Vive en grupos": True, "Brazos largos": True},
    "Orca": {"Grande": True, "Blanca y negra": True, "Caza en grupo": True},
    "Halcón": {"Vuela": True, "Rápido": True, "Tiene vista aguda": True},
    "Jirafa": {"Larga lengua": True, "Cuello largo": True, "Manchas": True},
    "Hipopótamo": {"Grande": True, "Vive en el agua": True, "Colmillos largos": True},
    "Canguro": {"Salta": True, "Bolsa marsupial": True, "Vive en Australia": True},
    "Lobo": {"Caza en manada": True, "Aúlla": True, "Pelaje gris": True},
    "Oso polar": {"Blanco": True, "Vive en el Ártico": True, "Nada en el agua helada": True},
    "Serpiente": {"Sin patas": True, "Piel escamosa": True, "Se desliza": True},
    "Mariposa": {"Tiene alas": True, "Vuela": True, "Tiene antenas": True},
    "Cocodrilo": {"Vive en el agua": True, "Tiene mandíbulas poderosas": True, "Piel escamosa": True},
    "Rana": {"Salta": True, "Verde": True, "Vive en el agua": True},
    "Búho": {"Nocturno": True, "Tiene plumas suaves": True, "Vuela silenciosamente": True},
    "Delfín": {"Vive en el mar": True, "Inteligente": True, "Nada rápido": True},
    "Zorro": {"Caza en solitario": True, "Pelaje rojizo": True, "Tiene cola larga": True},
    "Tiburón": {"Vive en el mar": True, "Tiene aletas dorsales": True, "Caza otros peces": True},
    "Panda": {"Blanco y negro": True, "Come bambú": True, "Vive en bosques de bambú": True},
    "Gato": {"Caza en solitario": True, "Felino": True, "Tiene bigotes": True},
    "Hormiga": {"Pequeña": True, "Vive en colonias": True, "Trabaja en equipo": True},
    "Ratón": {"Pequeño": True, "Come queso": True, "Vive en madrigueras": True},
    "Colibrí": {"Pequeño": True, "Tiene plumaje brillante": True, "Vuela hacia atrás": True},
    "Camaleón": {"Cambia de color": True, "Tiene ojos independientes": True, "Lengua larga": True}
}

# Función para realizar una pregunta y eliminar los animales que no cumplan con la característica
def pregunta(caracteristica, respuesta):
    global animales
    if respuesta:
        animales = {animal: atributos for animal, atributos in animales.items() if atributos.get(caracteristica)}
    else:
        animales = {animal: atributos for animal, atributos in animales.items() if not atributos.get(caracteristica)}

# Función para adivinar el animal
def adivinar():
    animal_adivinado = random.choice(list(animales.keys()))
    print("¡El animal es:", animal_adivinado, "!")

# Función principal del juego
def jugar_adivina_quien():
    print("Bienvenido al juego Adivina Quién - Edición de Animales!")
    print("Piensa en un animal y responde las preguntas con 's' para sí y 'n' para no.")
    print("Comencemos!")

    # Bucle para hacer preguntas hasta adivinar el animal
    while len(animales) > 1:
        caracteristica = random.choice(list(animales[random.choice(list(animales.keys()))].keys()))
        respuesta = input(f"¿Tu animal tiene la característica '{caracteristica}'? (s/n): ").lower()
        
        while respuesta != 's' and respuesta != 'n':
            respuesta = input("Por favor, responde 's' para sí o 'n' para no: ").lower()

        pregunta(caracteristica, respuesta == 's')

        if len(animales) > 1:
            print("Quedan", len(animales), "animales posibles.")

    if len(animales) == 1:
        adivinar()
    else:
        print("No quedan más animales para adivinar. ¿Quizás pensaste en un ser mitológico?")

# Iniciar el juego
jugar_adivina_quien()
