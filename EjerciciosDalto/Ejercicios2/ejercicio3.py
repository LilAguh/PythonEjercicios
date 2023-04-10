
'''
Escribir un programa que calcule una sucesion de Fibonacci
desde 0 hasta un numero especifico de terminos
'''

def fibonacci(num):
    a, b = 0, 1
    lista = [0]
    for i in range(num):
        if b > num:
            return lista
        else:
            lista.append(b)
            a, b = b, a + b

numero = fibonacci(22)
print(numero)