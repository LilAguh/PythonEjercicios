
'''
Tupla: es similar a una lista en cuanto a que también es una estructura de datos ordenada, 
pero a diferencia de las listas, las tuplas son inmutables, es decir, 
una vez creada no se pueden modificar. 
Para definir una tupla, se utilizan paréntesis () y se separan los elementos por comas.
'''

#Anteriormente la tupla la creamos de la siguiente manera:
tupla = tuple(['Aguh', 'Violeta'])

#Ahora, la tupla tambien puede ser definida de la siguiente manera:

tupla2 = 'Aguh', 'Violeta'

#De esta manera se crea una tupla con varios datos, 
# pero tambien se puede con un solo dato

tupla3 = 'Renault 9', #con solo poner una coma al final logramos realizar la tupla

#como ya sabemos la tupla es inmutable, esto nos beneficia
#utilizando un solo espacio en memoria, en las Listas utiliza
#un espacio por cada item almacenado.

print(tupla2)