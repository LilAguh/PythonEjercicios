
# Abrimos el archivo con with open
with open('Archivos/canciones.txt', encoding='UTF-8') as archivo:

    # Leemos el archivo
    contenido = archivo.read()

    # Mostramos el archivo
    print(contenido)

# No es necesario cerrar el archivo cuando se utiliza with open
