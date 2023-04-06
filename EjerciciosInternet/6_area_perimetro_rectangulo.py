
# 6_ Escribir un programa que calcule el área y el perímetro de un rectángulo dado su ancho y altura.

print('-------------------------------------------------')

print('Para calcular el area y el perimetro de un rectangulo necesitamos saber su base y su altura')
base = int(input('Medida de la base en centimetros: '))
altura = int(input('Medida de la altura en centimetros: '))


area = base * altura
perimetro = (base * 2) + (altura * 2)
    
print('-------------------------------------------------')

print(f'La base del rectangulo es de {base}cm y la altura de {altura}cm')
print(f'Su area es de {area}cm en total,')
print(f'Y su primetro es de {perimetro}cm.')

print('-------------------------------------------------')