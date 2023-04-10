'''
Creemos una funcion que al pasarle un numero nos genere numeros primos hasta
llegar a ese numero, por ejempolo:
si le pasamos el numero 15 nos devolveria [1, 2, 3, 5, 7, 11, 13]
'''
#Es una funcion en donde verifica si el numero es primo o no
def es_primo(num):
    for i in range(2, num - 1): #ejecutamos el bucle omitiendo el 1 y el propio numero
        if num % i == 0 : #Si el resto de la division entre numero y el numero de bucle es 0, retorna false
            return False
        i = i + 1
    return True


#Una funcion para integrar los numeros primos en una lista
def numeros_primos(num):
    primos = []
    for i in range(1,num + 1): #Ejecutamos el bucle entre 1 y un numero mas al numero ingresado
        primo = es_primo(i)
        if primo:
            primos.append(i) #Cargamos los numeros a la lista
        else:
            continue
    return primos #finalizado el bucle devuelve la lista con los numeros primos
    
print('------------------------------------------------------------')
numero = int(input('Hasta que numero quiere la lista de numeros primos?: '))
lista_de_numeros_primos = numeros_primos(numero)
print('La lista de numeros primos es:')
print(lista_de_numeros_primos)
print('------------------------------------------------------------')