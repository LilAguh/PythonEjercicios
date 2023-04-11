

# Si solo queremos agregar lineas usamos 'a' (adicion), no nos reescribe el contenido
with open('Archivos/canciones.txt', 'a', encoding='UTF-8') as archivo:

    # En este caso agregamos lineas, no sobreescribimos
    archivo.writelines('Si No Te Tengo - Ke Personajes\n')
