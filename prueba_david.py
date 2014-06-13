# -*- coding: utf8 -*-
import os

os.system("clear")

resp="s"
array=[]
while resp=="s":
	valor=raw_input("ingrese un valor >>>")
	array.append(valor)
	array.sort()
	valor2=raw_input("desea ingresar otro valor (s/n)>>")
	valor2.lower()
	resp=valor2
	os.system("clear")


for i in array:
	print i
