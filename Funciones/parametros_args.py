

print('-------------------------------------------------')
#Forma no optima de sumar valores
def suma1(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados
        
resultado = suma1([5, 3, 9, 12, 30])
print(resultado)

print('-------------------------------------------------')


#Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5, 3, 9, 12, 30, 68, 23, 36])
print(resultado2)

print('-------------------------------------------------')

#Utilizando el operador * como parametro (*args)
def suma2(nombre, *numeros):
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'
        
resultado = suma2('Aguh', 5, 3, 9, 12, 30, 68, 23, 36)
print(resultado)

print('-------------------------------------------------')
#Al parametro siempre lo debemos utilizar al final, porque no podriamos agregar mas
#El primer dato de los elementos, corresponde al primer parametro
#El resto al parametro args, debido a que se ejecuta infinita cantidad de veces


