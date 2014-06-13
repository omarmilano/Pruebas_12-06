#!/usr/bin/python

# Leonel Rojas Pérez
# C.I: 23.663.300

array=[]
a=raw_input("Ingrese primera palabra: ")
b=raw_input("Ingrese segunda palabra: ")
c=raw_input("Ingrese tercera palabra: ")

array.append(a)
array.append(b)
array.append(c)

array.sort()

for i in array:
	print i
