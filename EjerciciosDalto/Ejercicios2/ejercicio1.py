"""
Hoy falto el profesor de clases y los alumnos decidieron armar una clase propia,
uno de los alumnos hace las de profesor y otro es su asistente

1_ Pedir la edad de los compañeros que vinieron hoy a clase y ordenar 
los datos de menor a mayor

2_ El mayor de la clase es el profesor y el menor es el asistente, quien es quien?
"""

#Nombre y compañeros que vinieron hoy a clases
print('------------------------------------------------------------')


def obtener_companeros(cantidad_alumnos):
    companeros = []
    
    for i in range(cantidad_alumnos):
        print('------------------------------------')
        print('Ingresa el nombre del alumno:')
        nombre = input('')
        print('Ingresa la edad del alumno:')
        edad = int(input(''))
        companero = (nombre, edad)
        companeros.append(companero)
        
    companeros.sort(key = lambda x: x[1])
    asistente = companeros[0][0]
    profesor = companeros[-1][0]
    return profesor, asistente
    



print('Cuantos alumnos vinieron hoy a clase?:')
cantidad_alumnos = int(input(''))
profesor, asistente = obtener_companeros(cantidad_alumnos)

print('------------------------------------------------------------')
print(f'El profesor será {profesor}')
print(f'y su asistente {asistente}')
print('------------------------------------------------------------')
