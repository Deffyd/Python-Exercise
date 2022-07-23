#Escriba un algoritmo que pida al usuario el ingreso de números enteros y contabilice cuántos valores se ingresaron.
#El algoritmo debe solicitar números siempre y cuando el valor ingresado sea un dato positivo,
#si el usuario ingresa un número cero o negativo,debe finalizar el algoritmo e imprimir la cantidad total de números ingresados.


num1=int(input('Escribe número:'))



while num1 >= 0:
    print(len(str(num1)))
    num1=int(input('Escribe número:'))
    print(f'el número {num1} es positivo')
    if num1 == 0:
        print('El número es cero')
else:
    print('El numero es negativo ')

print('Fin Del Programa')