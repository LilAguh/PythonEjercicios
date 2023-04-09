
#Funciones integradas o Build In
#Estas como su nombre lo indica ya vienen integradas dentro
#del depurador de python

numeros = [1, 9, 2, 3, 12, 53, 55]

#Encontramos el numero mayor de una lista
#Solo funciona cuando los datos del iterable son numeros
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#Encontramos el numero menor de una lista
#Solo funciona cuando los datos del iterable son numeros
numero_mas_chico = min(numeros)
print(numero_mas_chico)

#redondeando a 4 decimales
#anteriormente vimos round pero sin utilizar el segundo elemento
#de la funcion que nos determina la cantidad de decimales
#que necesitamos en un numero flotante de gran longitud
pi = round(13.1415926535, 4)
print(pi)

#retorna false si le pasamos 0, un dato vacio, False o ningun dato
resultado_bool = bool(33)#Si le pasamos un dato da True
print(resultado_bool)

resultado_bool = bool(0)#Si le pasamos un 0 da False
print(resultado_bool)

resultado_bool = bool(False)#Si le pasamos un False da False
print(resultado_bool)

resultado_bool = bool(['Aguh', 'violeta'])#Si pasamos una lista da True
print(resultado_bool)

resultado_bool = bool()#Si le pasamos un dato vacio da False
print(resultado_bool)

resultado_bool = bool(-200)#Si le pasamos un numero negativo da True
print(resultado_bool)


#Retorna True si todos los valores son verdaderos
resultado_all = all([123, True, [133, 'Argentina']]) #El resultado es True porque todos los datos son verdaderos
print(resultado_all)

resultado_all = all([0, True, [133, 'Argentina']])#El resultado es False porque uno de sus datos (0) no es verdadero
print(resultado_all)


#Suma total de todos los valores de un iterable
#Solo funciona cuando los datos del iterable son numeros
suma_total = sum(numeros)
print(suma_total)
