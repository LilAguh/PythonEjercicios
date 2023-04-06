diccionario = {
    'nombre' : 'Aguh',
    'edad' : 24,
    'color_favorito' : 'violeta'
}

#devuelve las claves (tambien nos permite iterar)
clave = diccionario.keys()

#devuelve el valor de la clave
valor_clave = diccionario.get('color_favorito') 
#se le puede perdir directamente la clave 
#pero si no lo encuentra este mostraria un error,
#en cambio, con get, si no encuentra la clave esta muestra 
# un "none", algo similar a undefined en JavaScript 
#-------------------------------------------------------

#elimina un elemento 
diccionario.pop('edad') #tendria que eliminar la clave y el valor de "edad"

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
#practicamente transforma el diccionario en objeto iterable
print(diccionario_iterable)

#elimina todos los elementos del diccionario
diccionario.clear()
print(diccionario)