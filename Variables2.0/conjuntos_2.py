
'''Conjunto: es una estructura de datos no ordenada y mutable que se utiliza
para almacenar elementos únicos. No se pueden tener elementos 
duplicados en un conjunto. Para definir un conjunto, 
se utilizan llaves {} o la función set().'''

#Creamos un conjunto con Set

conjunto = set(['Dato1', 'Dato2'])

#podemos iterar el conjunto con datos no modificables como una tupla
#no asi con listas o diccionarios

conjunto2 = set(['Dato1', 'Dato2', ('DatoLista1', 'DatoLista2')])

#Metiendo un conjunto dentro de otro

conjunto3 = frozenset(['Dato3', 'Dato4'])
conjunto_iterado = {conjunto3,'Dato5'}

print(conjunto_iterado)

#----------------------------------------------------------------------

#Teoria de conjunto

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
print(resultado)

#Verificando con <=
resultado = conjunto2 <= conjunto1
print(resultado)

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
print(resultado)

#Verificando con >
resultado = conjunto2 > conjunto1
print(resultado)

#verificando si hay un numero en comun
resultado = conjunto2.isdisjoint(conjunto1) #Esto es True cuando ningun numero que se este comparando es igual
print(resultado)
