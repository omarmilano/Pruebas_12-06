#
# Nombres: Anderson Andres
# Apellidos: Guerrero Garcia
# C.I: 24390246
#
import math
print("Introduzca la operacion que se realizara.. ")
print("(1) Sumas")
print("(2) Restas")
print("(3) Multiplicacion")
print("(4) Divicion")
print("(5) Exponencial")
print("(6) Raiz")
op=int (raw_input("Introduzca la Seleccion.."))
A=0
B=0
if (op==1):
   A=float (raw_input("Introduzca Primer Numero.."))
   B=float (raw_input("Introduzca Segundo Numero.."))
   print("La Respuesta es: "+str(A+B))

if (op==2):
   A=float (raw_input("Introduzca Primer Numero.."))
   B=float (raw_input("Introduzca Segundo Numero.."))
   print("La Respuesta es: "+str(A-B))

if (op==3):
   A=float (raw_input("Introduzca Primer Numero.."))
   B=float (raw_input("Introduzca Segundo Numero.."))
   print("La Respuesta es: "+str(A*B))

if (op==4):
   A=float (raw_input("Introduzca Primer Numero.."))
   B=float (raw_input("Introduzca Segundo Numero.."))
   print("La Respuesta es: "+str(A/B))


if (op==5):
   A=float (raw_input("Introduzca el Numero.."))
   B=float (raw_input("Introduzca el Exponente.."))
   
   cont=2
   while cont <=B:
	   A=A*A 
	   cont=cont+1
	   
   print("El Resultado es: "+str(A))   

if (op==6):
   A=float (raw_input("Introduzca el Numero.."))
   print("La Respuesta es: "+str(math.sqrt(A)))



