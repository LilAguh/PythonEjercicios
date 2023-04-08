
#Esto funciona tanto para lista como para tuplas, como para conjuntos
animales = ['perro', 'loro', 'gato', 'cocodrilo']
numeros = [52, 12, 55, 23]

#Recorriendo la lista annimales
for animal in animales:
    print(f'Ahora la variable animal pertenece a: {animal}')
    
#Recorriendo la lista numeros y multiplicar su valor x10
for numero in numeros:
    resultado = numero * 10
    print(f'El N:{numero} multiplicado x10 es igual a {resultado}')
    
#Recorriendo 2 listas del mismo tamano al mismo tiempo
for numero, animal in zip(animales,numeros):
    print(f'recorriendo la lista 1= {animal}')
    print(f'recorriendo la lista 2= {numero}')
    
#Forma crear el bucle x cantidad de veces
for num in range(20):
    print(num)
    
#Forma no optima de recorrer una lista, y si recorremos un conjunto el codigo se rompe
for num in range(len(numeros)):
    print(numeros[num])
    
#Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
#Usando else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('el bucle termino')
    