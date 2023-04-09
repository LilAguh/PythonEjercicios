
print('-------------------------------------------------')
#La posicion en la que se ubican los parametros es clave para
#El orden en la que se llama la funcion, por eso se mandan de manera ordenada
def frase (nombre, apellido, adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}.'

#Pero en caso de evitar errores es mejor pasarlos por medios de clave - valor
#En donde el orden no perjudica el funcionamiento de la funcion
frase_resultado = frase(adjetivo = 'fachero', nombre = 'Aguh', apellido = 'Ochoa')
print(frase_resultado)

print('-------------------------------------------------')

#Creando la misma funcion pero con un parametro opcional con un valor por defecto
def frase (nombre, apellido, adjetivo = 'tonto'):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}.'

#El parametro por defecto tiene el valor "tonto"
#Asi que no es necesario pasar el valor de adjetivo en el parametro
#Pero en caso de agregarlo este es remplaazado por el cual nosotros ingresamos
frase_resultado = frase('Aguh', 'Ochoa', 'fachero')
print(frase_resultado)

print('-------------------------------------------------')