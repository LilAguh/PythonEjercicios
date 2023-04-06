"""---------------Transcripcion-------------------"""
"""
1_El timing para ver los conceptos vistos en Python
en un curso de corrido es de 2.5 horas como minimo,
7 horas como maximo y 4 horas en promedio.
Este curso lo logro en una hora y media.

    *Cuanta diferencia en porcentajes hay entre el curso actual
    y el mas rapido de los otros cursos?
    *El mas lento de los otros cursos
    *El promedio de los cursos
    
2_Teniendo en cuenta que la cantidad de crudo en 
promedio de los demas cursos es de 5 horas, y con
edicion lo convierten en 4 horas y el crudo de este
video fue de 3:30 horas, y se redujo a 1:30 horas

    *Que porcentaje de material inservible se reduce
    en los crudos en ambos casos?

3_
    *Ver 10 horas de este curso, seria equivalente a
    cuantas horas de los otros cursos?
    *Ver 10 horas de los otros cursos a cuantas horas
    de este curso equivale?
"""
print('-------------------------------------------------')

#1_ Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_avg = 4
este_curso = 1.5

#diferencias de duracion
diferencias_min = 100 - (este_curso / otros_cursos_min * 100)
diferencias_max = 100 - (este_curso * 1000 // otros_cursos_max / 10)
diferencias_avg = 100 - (este_curso / otros_cursos_avg * 100)

print(f'El promedio con el curso mas rapido es de {diferencias_min}%')
print(f'El promedio con el curso mas lento es de {diferencias_max}%')
print(f'El diferencia con el promedio del resto es de {diferencias_avg}%')
print('-------------------------------------------------')


#2_ Promedio de crudo
crudo_promedio_otros = 5
editado_promedio_otros = 4
crudo_este_video = 3.5 #.35
editado_este_video = 1.5 # 1500

#promedio material desperdiciado
diferencia_crudo_otros = 100 - (editado_promedio_otros / crudo_promedio_otros * 100)
diferencia_crudo_dalto = 100 - (editado_este_video * 1000 // crudo_este_video / 10)

print(f'El desperdicio de material de los otros cursos es de aproximadamente el {diferencia_crudo_otros}%')
print(f'Mientras que el promedio de desperdicio en este curso es del {diferencia_crudo_dalto}%')
print('-------------------------------------------------')


#3_Equivalencias entre los cursos

equivalente_otros_cursos = (otros_cursos_avg * 100 // este_curso / 10)
equivalente_este_curso = (este_curso * 100 // otros_cursos_avg / 10)

print(f'Ver 10 horas de este curso equivalen a {equivalente_otros_cursos} horas de otro curso')
print(f'Y ver 10 horas de otro curso, equivalen a {equivalente_este_curso} horas de este curso')
print('-------------------------------------------------')