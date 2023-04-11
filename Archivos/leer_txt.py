
# Usando open para abrir el archivo con una codificacion universal utf-8
archivo = open('Archivos/canciones.txt', encoding='UTF-8')

# Leer archivo completo:
# archivo = archivo_sin_leer.read()

# Leer linea por linea
# lineas = archivo_sin_leer.readlines()

# Leer una sola linea
linea = archivo.readline()

# Cerrar el archivo
# Es importante cerrarlo porque se puede corromper, ademas windows no permite abrir el mismo archivo en multiples lugares
archivo.close()

print(linea)
