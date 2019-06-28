#Enrique Lira Martinez A01023351 Tortas
import random
import math
from collections import Counter
from statistics import mode

lista=[]
lista2= []
lista4= []
lista6= []
lista8= []
lista10= []
lista12= []
valores = []
comprados=0

for j in range(0,49999):
	valorT=0
	a=random.randint(1,100)
	n_tortas_compradas = random.randint(0,12)
	vendidos = n_tortas_compradas * 12
#	vendidos=random.randint(0,144)
	if a >=  1 and a <= 5:
		comprados=2*12
		if comprados > vendidos:
			valorT=(vendidos*45)+(comprados-vendidos/2*1.5)-comprados*(18)-vendidos*(2)
		elif comprados < vendidos:
			valorT=(comprados*45)-10*(vendidos-comprados)-comprados*(18)-comprados*(2)
		else:
			valorT=(vendidos*45)-vendidos*(18)-vendidos*(2)
		lista2.append(valorT)	
	elif a >=  6 and a <= 15:
		comprados=4*12
		if comprados > vendidos:
			valorT=(vendidos*45)+(comprados-vendidos/2*1.5)-comprados*(18)-vendidos*(2)
		elif comprados < vendidos:
			valorT=(comprados*45)-10*(vendidos-comprados)-comprados*(18)-comprados*(2)
		else:
			valorT=(vendidos*45)-vendidos*(18)-vendidos*(2)
		lista4.append(valorT)	
	elif a >=  16 and a <= 35:
		comprados=6*12
		if comprados > vendidos:
			valorT=(vendidos*45)+(comprados-vendidos/2*1.5)-comprados*(18)-vendidos*(2)
		elif comprados < vendidos:
			valorT=(comprados*45)-10*(vendidos-comprados)-comprados*(18)-comprados*(2)
		else:
			valorT=(vendidos*45)-vendidos*(18)-vendidos*(2)	
		lista6.append(valorT)	

	elif a >=  36 and a <= 75:
		comprados=8*12
		if comprados > vendidos:
			valorT=(vendidos*45)+(comprados-vendidos/2*1.5)-comprados*(18)-vendidos*(2)
		elif comprados < vendidos:
			valorT=(comprados*45)-10*(vendidos-comprados)-comprados*(18)-comprados*(2)
		else:
			valorT=(vendidos*45)-vendidos*(18)-vendidos*(2)
		lista8.append(valorT)	
	
	elif a >=  76 and a <= 95:
		comprados=10*12
		if comprados > vendidos:
			valorT=(vendidos*45)+(comprados-vendidos/2*1.5)-comprados*(18)-vendidos*(2)
		elif comprados < vendidos:
			valorT=(comprados*45)-10*(vendidos-comprados)-comprados*(20)
		else:
			valorT=(vendidos*45)-vendidos*(20)
		lista10.append(valorT)	

	elif a >=  96 and a <= 100:
		comprados=12*12
		if comprados > vendidos:
			valorT=(vendidos*45)+(comprados-vendidos/2*1.5)-comprados*(18)-vendidos*(2)
		elif comprados < vendidos:
			valorT=(comprados*45)-10*(vendidos-comprados)-comprados*(18)-comprados*(2)
		else:
			valorT=(vendidos*45)-vendidos*(18)-vendidos*(2)
		lista12.append(valorT)	
	lista.append(valorT)	

print("Para 0 a 2 su ganancia es de :",sum(lista2) / len(lista2))
print("Para 3 a 4 su ganancia es de :",sum(lista4) / len(lista4))
print("Para 5 a 6 su ganancia es de :",sum(lista6) / len(lista6))
print("Para 7 a 8 su ganancia es de :",sum(lista8) / len(lista8))
print("Para 9 a 10 su ganancia es de :",sum(lista10) / len(lista10))
print("Para 11 a 12 su ganancia es de :",sum(lista12) / len(lista12))



