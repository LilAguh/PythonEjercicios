#En este archivo se importan los modulos, pero
#ahora se encuentran dentro de una carpeta, exterma al modulo


#Tenemos que importar el Modulo sys
#Se utiliza para saber el nombre de los modulos builtind disponibles
import sys
# print(sys.builtin_module_names)

#Se utiliza para saber la ruta de los modulos
# print(sys.path)

#Con esta funcion nos introducimos a la ubicacion del modulo
sys.path.append('/home/lety/MyDevHistory/repos/Python/PythonEjercicios/Funciones_Modulos')
from modulo_saludar import saludar, saludo_nashe

print(saludar('LilAguh'))
print(saludo_nashe('LilAguh'))