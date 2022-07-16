#Escribir el algoritmo que permita ingresar el sueldo a pagar para un grupo de 30 empleados,
#determine el sueldo promedio y el sueldo menor

lista_sueldos=[]
cont=1


while cont <= 3: 
    if len(lista_sueldos) <= len(lista_sueldos):
        lista_sueldos.append(int(input('Ingresar el sualdo:')))
    cont+=1

suma=sum(lista_sueldos)

promedio_sueldos=suma//len(lista_sueldos)

print(f'La suma de todos los sualdos es: {suma}')
print(f'El promedio de los sueldos es: {promedio_sueldos}')
print(f'El sueldo menor es: {min(lista_sueldos)}')