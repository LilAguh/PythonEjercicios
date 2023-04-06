
# 3_ Escribir un programa que lea un número entero desde el teclado y determine si es par o impar.

print('-------------------------------------------------')

print('Ingresa 1 numero en consola para saber si es par o impar:')
numero = int(input(''))

if numero % 2 == 0:
    resultado = 'es par'
else:
    resultado = 'es impar'
    
print('-------------------------------------------------')

print(f'El numero {numero} es {resultado}.')

print('-------------------------------------------------')