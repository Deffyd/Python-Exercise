#Crea un programa que pregunte a los trabajadores de una empresa su nombre y el total de sus ventas realizadas en el mes
#luego calcule el 13% de las ventas y davuelva el nombre del empleado junto a un mensaje y el porcentaje de ventas

nombre = input('¿Cual es tu nombre?: ')

ventas = float(input('¿Cual es tu cantidad de ventas?: $'))

porcentaje = ventas*13/100

print (f'Hola {nombre}\n Tu comision del mes por los ${ventas} de ventas es ${round(porcentaje,2)}')