
#Creando una Lista
lista = ["Aguh", "LilAguh", False, 1.71] #la li[sta es modificable
print(lista[3]) #1.71

#Creando una Tupla
tupla = ("Aguh", "LilAguh", False, 1.71) #la tupla no se puede modificar
print(lista[0]) #Aguh

#Esto es correcto
lista[0] = "Aguh"

#Esto es incorrecto
#tupla[0] = "Aguh"

#Creando un Conjunto(set)
conjunto = {"Aguh", "LilAguh", False, 1.71} #es modificable pero no los elementos
print(conjunto) #A{"Aguh", "LilAguh", False, 1.71} 

#no puedo acceder al indice del conjunto y tampoco es posible repetir los datos
#es practicamente una cadena de datos desordenada que elimina repetidos

#Creando un diccionario (simialar a un Json), practicamente un objeto
# siempre es "Key" : "Value",
diccionario = {
    "nombre" : "Aguh",
    "github" : "LilAguh",
    "empleado": False,
    "altura" : 1.71,
    "dato_duplicado" : "Aguh"
}
print(diccionario["nombre"])