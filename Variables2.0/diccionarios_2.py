'''
Diccionario: es una estructura de datos que se utiliza para almacenar
pares clave-valor, donde cada clave es única y tiene asociado un valor. 
Los elementos de un diccionario no están ordenados y son mutables. 
Para definir un diccionario, se utilizan llaves {} y 
se separan los pares clave-valor por comas. 
'''
#Creando un diccionario
diccionario = {
    'nombre' : 'Aguh',
    'color' : 'Violeta'
}

#Creando un diccionario con dict()
diccionario = dict(nombre = "Aguh", color = "Violeta") #Si necesitamos crear diccionarios vacios esta es la unica forma

#Las listas no pueden ser claves porque son iterables
#En cambio las tuplas si pueden ser claves
diccionario = {
    ('tupla1', 'tupla2') : 'diccionario'
}

#Y para meter conjuntos necesitamos de "frozenset"
diccionario = {
    frozenset(['tupla1', 'tupla2']) : 'diccionario'
}
#------------------------------------------------------

#Creando un diccionario con dict.fromkeys()
diccionario = dict.fromkeys(['nombre','apellido','color','pais']) #Tiene que escribirse en forma de lista
#Esta tecnica sirve para crear un diccionario con valores "None"

#Tambien nos sirve para pasarle un primer valor con datos iterable y nos iguala al segundo valor ingresado
diccionario = dict.fromkeys('ABCDE', True)# {'A': True, 'B': True, 'C': True, 'D': True, 'E': True}

#Como primer valor se le puede ingresar una lista tambien
diccionario = dict.fromkeys(['nombre','apellido'], 'No se sabe')#{'nombre': 'No se sabe', 'apellido': 'No se sabe'}


print(diccionario)