
#Importamos el archivo que contenga la funcion necesaria
#Con as le asignamos un nombre al modulo, como en React
#import saludar from modulo_saludar
#Ese es el equivalente en React
#Se llaman NameSpace
import modulo_saludar as saludar

#La inicializamos como si fuera un metodo
saludo = saludar.saludar('Aguh')
print(saludo)

#Ahora si queremos importar solamente una funcion si pomenos
#De esta manera nos ahorramos importar el componente entero y solo importamos las funciones
from modulo_saludar import saludar, saludo_nashe
print(saludar('LilAguh'))
print(saludo_nashe('LilAguh'))

#Accedemos al nombre de este modulo
print(__name__)

#Accedemos al nombre del modulo llamado
print(saludar.__name__)