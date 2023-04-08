
frutas = ['banana', 'manzana', 'ciruela', 'pera', 'naranja', 'uva', 'durazno']
cadena = 'Que onda la banda'
numeros =[2, 4, 5, 10]

#Evitando comer una ciruela con la sentencia continue
for fruta in frutas:
    if fruta == 'ciruela':
        continue
    print(f'Me voy a comer una {fruta}')
    
print('--------------------------------------------')
    
#Evitando comer una pera y el resto de frutas con la sentencia breack (un else tampoco se ejecuta)
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'pera':
        break
print('No como mas, me descompuse culpa de la pera')

print('--------------------------------------------')

#Recorrer una cadena de texto
for letra in cadena:
    print(letra)

print('--------------------------------------------')

#For en una lista en una linea
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)