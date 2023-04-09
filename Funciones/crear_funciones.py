
#Creando una funcion simple
# def saludar():
#    print("Que onda perraca")
    
#Ejecutando la funcion
#saludar()
print('-------------------------------------------------')
#Crear una funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if sexo == 'mujer':
        adjetivo = 'reina'
    elif sexo == 'hombre':
        adjetivo = 'rey'
    else:
        adjetivo = 'helicoptero apache de combate preferido'
    print(f'Hola {nombre}, como andas mi {adjetivo}?')
    
saludar('Mateo', 'master')

print('-------------------------------------------------')
#Crear una funcion que retorne valores
def crear_contrasena_random(num):
    chars = 'abcdefghij'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f'{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}'
    return contrasena
    
password = crear_contrasena_random(68)
frase = f'Tu nueva contrasena es: {password}'
print(frase)

print('-------------------------------------------------')
#Crear una funcion que retorne multiples valores
def crear_contrasena_random(num):
    chars = 'abcdefghij'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f'{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}'
    return contrasena, num

#Desempaquetamos la 
password, primer_numero = crear_contrasena_random(68)
print(f'Tu nueva contrasena es: {password}')
print(f'El numero utilizado para crearla fue: {primer_numero}')

print('-------------------------------------------------')