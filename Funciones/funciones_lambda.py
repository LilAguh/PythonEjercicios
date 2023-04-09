
numeros = [1, 12, 9, 22, 34, 54]

print('-------------------------------------------------')
#Es algo bastante similar a las arrow functions de JavaScript
multiplicar_por_dos = lambda numero : numero * 2
#multiplicarPorDos = numero => numero * 2

print(multiplicar_por_dos(10))

print('-------------------------------------------------')
#Tiene el mismo concepto que las arrow functions
#Se utiliza pora instrucciones simples

#---------------------------------------------------------------------------------

#Creando funcion comun que diga si es par o no
def es_par(num):
    if(num % 2 == 0):
        return True

#Usando filter con una funcion comun
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))

print('-------------------------------------------------')

#Creando lo mismo pero en funcion lambda
numeros_pares_lambda = filter(lambda numero : numero % 2 == 0, numeros)
print(list(numeros_pares_lambda))

#Creamos la funcion y la ejecucion en una sola linea
