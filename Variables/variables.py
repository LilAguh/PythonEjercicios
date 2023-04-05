
#Definiendo variables
""" 
    Mucho muy inportante
    En Python las variables se declaran en snake_case
    ej: nombre_de_una_variable
    Caso JavaScript es mas recomendable declarar en camelCase
    ej: nombreDeUnaVariable
    
    acordate genio
"""

a = 400
b = 20
c = a + b

print(c)

nombre = "Aguh"
print(nombre)

#Concatenacion con operadores

bienvenida = "Hola " + nombre + ", como estas?"
print(bienvenida)

#Concatenacion con f-strings

concatenacion_de_datos = f"{c} es un dato numerico y {nombre} es mi nombre"
print(concatenacion_de_datos)

# Operadores de pertenencia (in, Not in, is, Not is)

print("ola" in bienvenida)  #True, porque ola esta dentro del string bienvenida
print("ola" is bienvenida)  #False, porque ola no es el string bienvenida