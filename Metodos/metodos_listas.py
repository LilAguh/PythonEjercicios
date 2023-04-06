

#creando una lista con list
lista = list(["Aguh", "LilAguh", False, 1.71])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append('Belgrano')

#agrega elementos en un indice especifico
lista.insert(2, 'Violeta')

#agregar varios elementos en una lista
lista.extend(['Frio', 'Renault 9', 'BMW e46', '1999'])

#eliminando elemento por su inice
lista.pop(8) #elimina el elemento 'BMW e46'
lista.pop(-1) #elimina el ultimo elemento de la lista

#elimina un elemento de la lista y devuelve un valor
lista.remove(False) #elimina el False de la lista, debe estar si o si el elemento

#--------------------------------------------------------#
lista2 = [123, 12, 24, 54, 1223, 24, True, True, False, 765]

#ordenando la lista de forma ascendente
lista2.sort()#(si usamos reverse=True se ordena en forma descendiente)

#invirtiendo los elementos de una lista
lista2.reverse()

#eliminando todos los elementos de la lista
lista2.clear()

print(lista2)