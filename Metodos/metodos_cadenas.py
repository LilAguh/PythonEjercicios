cadena1 = "queondalabanda"
cadena2 = "el unico grande de cba es Belgrano"
cadena3 = "123123"

#convierte todo a mayusculas
mayusculas = cadena1.upper()

#convierte todo a minusculas
minusculas = cadena1.lower()

#convierte la primer letra de la cadena a mayusculas
primera_a_mayus= cadena1.capitalize()

#buscamos una cadena en otra cadena, devuelve -1 si no existe coincidencias
busqueda_find = cadena2.find("B") #devolveria el valor 26
busqueda_find2 = cadena2.find("z") #devolveria el valor -1 porque no existe

#buscamos una cadena en otra cadena
busqueda_index = cadena2.find("B") #devolveria el valor 26
busqueda_index2 = cadena2.find("z") #devolveria una excepcion (error)

#Si es numerico devuelve true, si no False
es_numerico = cadena2.isnumeric() #devuelve false, no es un valor numerico
es_numerico2 = cadena3.isnumeric() #devuelve true, es un string pero contiene solo numeros

#si es alfanumerico devuelve true, si no False
es_alfa = cadena1.isalpha() #devuelve true, es afanumerico, es decir solo letras de la a a la z sin la ñ o tildes o espacios
es_alfa2 = cadena3.isalpha() #devuelve false, no es alfanumerico

#buscamos una cadena en una cadena, vevuelve la cantidad de veces que coincida
contar_coincidencias = cadena2.count("a") #devuelve 3 porque solo hay tres coincidencias
contar_coincidencias2 = cadena2.count("Bel") #devuelve 1 porque solo hay una  coincidencia

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1) #devuelve 14, tiene esa cantidad de caracteres

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena2.startswith("e") #true
empieza_con2 = cadena2.startswith("b") #false

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena2.endswith("e") #false
termina_con2 = cadena2.endswith("no") #true

#reemplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena2.replace("cba", "argentina") #devuelve "el mas grande de argentina es Belgrano"
cadena_nueva2 = cadena3.replace("1", " ") #reemplaza el 1 por un espacio

#separa la cadena con la cadena que le pasemos
cadena_separada = cadena2.split(" ") #en este caso separamos la cadena, por los espacios

print(cadena_separada)