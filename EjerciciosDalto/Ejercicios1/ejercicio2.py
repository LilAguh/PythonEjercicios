"""---------------Transcripcion-------------------"""
"""
Suponiendo que cada persona promedio habla 2 palabras por segundo

1_  Pedirle al usuario que diga cualquier texto real y que 
    *Calcular cuanto se tardaria en decir esa frase
    *Cuantas palabras dijo
    
2_  Si se tarda mas de 1 minuto decirle:
    "Para flaco, tampoco te pedi un testamento"
    
3_  Teniendo en cuenta que Dalto habla un 30% mas tapido
    *Cuanto tardaria en decir el mismo texto?
"""
print('-------------------------------------------------')

#1 Texto, duracion y cantidad de palabras

print('Tirame un texto genio:')
texto = input('').split(' ')
cantidad_palabras = len(texto)
tiempo_en_segundos = cantidad_palabras / 2

print('-------------------------------------------------')

#2_ Para flaco, tampoco te pedi un testamento

tiempo_en_minutos = tiempo_en_segundos * 10 // 60 / 10

if tiempo_en_segundos > 60:
    print(f'Para flaco, tampoco te pedi un testamento')
    print(f'Me dijiste {cantidad_palabras} palabras en {tiempo_en_minutos} minutos')
else:
    print(f'Me dijiste {cantidad_palabras} palabras en {tiempo_en_segundos} segundos')

print('-------------------------------------------------')

#3_ Dalto lo diria en...

dalto_lo_diria = (tiempo_en_segundos * 100) // 1.3 / 100

print(f'Esto Dalto lo hubiese dicho en {dalto_lo_diria} segundos mas o menos')
print('-------------------------------------------------')