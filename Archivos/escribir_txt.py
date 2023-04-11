
# En este caso agregamos 'w' (write), para escribir en el archivo
# Ademas con el permiso 'w' si no encuentra el archivo lo crea
with open('Archivos/canciones.txt', 'w', encoding='UTF-8') as archivo:

    # El comando sobreescribe el archivo (Caution culeado)
    # archivo.write('Si No Te Tengo - Ke Personajes')

    # El comando sobreescribe le archivo pero con posibilidad de agregar linea por linea
    archivo.writelines('Milagrosa - Milo J\n')
    archivo.writelines('hARAkiRi - Duki, C.R.O\n')
