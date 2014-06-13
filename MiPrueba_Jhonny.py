# -*- coding: utf8 -*-
#Jhonny Córdova. C.I.:20990499
# Realizar un programa que permita hacer uso de las operaciones matemáticas básicas
# y además exponentes y raices

def exponente(x, e):
    return x**e

def raiz(x):
    import math

    return math.sqrt(x)

def suma(x,y):
    return x+y

def resta(x,y):
    return x-y
    
def multiplica(x,y):
    return x*y
    
def divide(x,y):
    if y > 0:
        return x/y
    else: 
        print 'No es divisible, es infinito'

mensaje = "Programa para Operaciones Basicas"
menu = "1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Exponencial \n 6. Raiz Cuadrada"

print mensaje
print menu
resp = "S"
while resp == "S" or resp == "s":

	opc = int(raw_input("Ingrese el Numero de su opcion: "))

	if opc == 1:
		numero1 = int(raw_input("Ingrese Numero: "))
		numero2 = int(raw_input("Ingrese Otro Numero: "))

		print "La Suma de los numeros dados es: " + str(suma(numero1,numero2))
		resp = raw_input("Desea Realizar Otra Operación: (S/N)")


	elif opc == 2:
		numero1 = int(raw_input("Ingrese Numero: "))
		numero2 = int(raw_input("Ingrese Otro Numero: "))

		print "La Resta de los numeros dados es: " + str(resta(numero1,numero2))
		resp = raw_input("Desea Realizar Otra Operación: (S/N)")

	elif opc == 3:
		numero1 = int(raw_input("Ingrese Numero: "))
		numero2 = int(raw_input("Ingrese Otro Numero: "))

		print "La Multiplicacin de los numeros dados es: " + str(multiplica(numero1,numero2))
		resp = raw_input("Desea Realizar Otra Operación: (S/N)")

	elif opc == 4:
		numero1 = int(raw_input("Ingrese Numero: "))
		numero2 = int(raw_input("Divido entre: "))

		print "La Division es: " + str(divide(numero1,numero2))
		resp = raw_input("Desea Realizar Otra Operación: (S/N)")


	elif opc == 5:
		numero1 = int(raw_input("Ingrese Numero: "))
		numero2 = int(raw_input("Exponenciado a: "))

		print "La Exponenciación es: " + str(exponente(numero1,numero2))
		resp = raw_input("Desea Realizar Otra Operación: (S/N)")

	elif opc == 6:
		numero1 = int(raw_input("Ingrese Numero: "))

		print "La Raiz Cuadrada es: " + str(raiz(numero1))
		resp = raw_input("Desea Realizar Otra Operación: (S/N)")
	else:
		print "Esa No es una Opción Correcta"
		resp = raw_input("Desea Realizar Otra Operación: (S/N)")


