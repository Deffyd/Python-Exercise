#Diseñe un algoritmo para ingresar por teclado 2 números enteros, Si el primer valor ingresado es el mayor,
#realice la resta entre ellos, si no, muestre el valor mayor. 



n1 = int(input('Escribe el primer número: '))

n2 = int(input('Escribe el segúndo número: '))

if n1 > n2:
    print(n1-n2)
else:
    print(n1)
print('Fin del programa')
