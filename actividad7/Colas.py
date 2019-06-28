#Enrique Lira Martinez A01023351 Colas
import random
import math
from collections import Counter
from statistics import mode
import numpy as np
import scipy as sp
import scipy.stats
import matplotlib.pyplot as plt

def TiempoLlegadas():
	probabilidad = random.randint(1, 100)
	if(probabilidad <= 2):
		minutos = 20
	if(probabilidad > 2 and probabilidad <= 10):
		minutos = 25
	if(probabilidad > 10 and probabilidad <= 22):
		minutos = 30
	if(probabilidad > 22 and probabilidad <= 47):
		minutos = 35
	if(probabilidad > 47 and probabilidad <= 67):
		minutos = 40
	if(probabilidad > 67 and probabilidad <= 82):
		minutos = 45
	if(probabilidad > 82 and probabilidad <= 92):
		minutos = 50
	if(probabilidad > 92 and probabilidad <= 97):
		minutos = 55
	if(probabilidad > 97 and probabilidad <= 100):
		minutos = 60
	return minutos

def TiempoServicio3():
	probabilidad = random.randint(1, 100)
	if(probabilidad <= 5):
		minutos = 20
	if(probabilidad > 5 and probabilidad <= 15):
		minutos = 25
	if(probabilidad > 15 and probabilidad <= 35):
		minutos = 30
	if(probabilidad > 35 and probabilidad <= 60):
		minutos = 35
	if(probabilidad > 60 and probabilidad <= 72):
		minutos = 40
	if(probabilidad > 72 and probabilidad <= 82):
		minutos = 45
	if(probabilidad > 82 and probabilidad <= 90):
		minutos = 50
	if(probabilidad > 90 and probabilidad <= 96):
		minutos = 55
	if(probabilidad > 96 and probabilidad <= 100):
		minutos = 60
	return minutos

def TiempoServicio4():
	probabilidad = random.randint(1, 100)
	if(probabilidad <= 5):
		minutos = 15
	if(probabilidad > 5 and probabilidad <= 20):
		minutos = 20
	if(probabilidad > 20 and probabilidad <= 40):
		minutos = 25
	if(probabilidad > 40 and probabilidad <= 60):
		minutos = 30
	if(probabilidad > 60 and probabilidad <= 75):
		minutos = 35
	if(probabilidad > 75 and probabilidad <= 87):
		minutos = 40
	if(probabilidad > 87 and probabilidad <= 95):
		minutos = 45
	if(probabilidad > 95 and probabilidad <= 99):
		minutos = 50
	if(probabilidad > 99 and probabilidad <= 100):
		minutos = 55
	return minutos
	
def TiempoServicio5():
	probabilidad = random.randint(1, 100)
	if(probabilidad <= 10):
		minutos = 10
	if(probabilidad > 10 and probabilidad <= 28):
		minutos = 15
	if(probabilidad > 28 and probabilidad <= 50):
		minutos = 20
	if(probabilidad > 50 and probabilidad <= 68):
		minutos = 25
	if(probabilidad > 68 and probabilidad <= 78):
		minutos = 30
	if(probabilidad > 78 and probabilidad <= 86):
		minutos = 35
	if(probabilidad > 86 and probabilidad <= 92):
		minutos = 40
	if(probabilidad > 92 and probabilidad <= 97):
		minutos = 45
	if(probabilidad > 97 and probabilidad <= 100):
		minutos = 50
	return minutos

def TiempoServicio6():
	probabilidad = random.randint(1, 100)
	if(probabilidad <= 12):
		minutos = 5
	if(probabilidad > 12 and probabilidad <= 27):
		minutos = 10
	if(probabilidad > 27 and probabilidad <= 53):
		minutos = 15
	if(probabilidad > 53 and probabilidad <= 68):
		minutos = 20
	if(probabilidad > 68 and probabilidad <= 80):
		minutos = 25
	if(probabilidad > 80 and probabilidad <= 88):
		minutos = 30
	if(probabilidad > 88 and probabilidad <= 94):
		minutos = 35
	if(probabilidad > 94 and probabilidad <= 98):
		minutos = 40
	if(probabilidad > 98 and probabilidad <= 100):
		minutos = 45
	return minutos
resultadoC =[]
resultadoO =[]
resultadoE =[]
resultado = {'tiempoEntreLlegada': 0,'tiempoLlegada': 0,'inicioServicio': 0,'tiempoServicio': 0,'terminoServicio': 0, 'ocio': 0, 'espera': 0,'longitud': 0}
horaComida = 900
comida = False
totalesperaF =0
dia =0
totalespera =0
tiempoEntreLlegada =0
tiempoServicio = 0
terminoServicio =0
espera =0
personas =6
horaExtra=0
Salario=0
Almacen =0
ocio=0
ocio_total=0
costo =0
longitudCola = 1
inicio=0
inicioServicio =0
tiempoLlegada =0
for i in range(5000):
	while dia <= 30:
		while tiempoLlegada < 1440:
			resultado['inicioServicio'] = divmod(inicioServicio, 60)
			resultado['tiempoEntreLlegada'] = tiempoEntreLlegada
			resultado['tiempoLlegada'] = divmod(tiempoLlegada, 60)
			resultado['espera'] = espera
			resultado['ocio'] = ocio
			resultado['longitudCola'] = longitudCola
			tiempoEntreLlegada=TiempoLlegadas()
			tiempoLlegada += tiempoEntreLlegada 
			if(personas == 6):
				tiempoServicio = TiempoServicio6()
			elif (personas == 5):
				tiempoServicio = TiempoServicio5()
			elif (personas == 4):
				tiempoServicio = TiempoServicio4()
			elif (personas == 3):
				tiempoServicio = TiempoServicio3()
						
			terminoServicio = inicioServicio + tiempoServicio
			resultado['tiempoServicio'] = tiempoServicio
			resultado['terminoServicio'] = divmod(terminoServicio, 60)
			if(terminoServicio > inicio+480):
				horaExtra = (terminoServicio-inicioServicio)/60 * 37.5 * personas
				Salario = 8*25* personas
				Almacen = ((terminoServicio-inicioServicio) + 480) / 60 * 500
				totalesperaF = totalespera/60 * 100
				costo += horaExtra+Salario+Almacen+totalespera		
				inicio = terminoServicio
			if (tiempoLlegada < terminoServicio):
				if(terminoServicio >= horaComida and comida == False):
					inicioServicio = terminoServicio + 30
					comida = True
				else:
					inicioServicio = terminoServicio
				ocio = 0
				espera = inicioServicio - tiempoLlegada
				totalespera += espera
			else:
				if(tiempoLlegada >= horaComida and comida == False):
					inicioServicio = tiempoLlegada + 30
					comida = True
				else:
					inicioServicio = tiempoLlegada
				espera = 0
				ocio =tiempoLlegada-terminoServicio
				ocio_total += ocio
		inicio=tiempoLlegada -1440
		inicioServicio =tiempoLlegada -1440
		tiempoLlegada =tiempoLlegada -1440
		dia += 1
	resultadoC.append(costo/30)
	resultadoO.append(ocio_total/30)
	resultadoE.append(totalespera/30)
	dia = 0
	costo = 0
	ocio_total =0
	totalespera =0
print("Equipos de", personas,"personas") 
print("Costo Promedio:", sum(resultadoC) / float(len(resultadoC)) )
print("Tiempo de ocio promedio",sum(resultadoO) / float(len(resultadoO)),"hrs")
print("Tiempo de espera promedio",sum(resultadoE) / float(len(resultadoE)),"hrs")

#Costo Promedio: 1,080,602.843266665 -------6 personas
#Costo Promedio: 3,272,095.37-------5 personas
#Costo Promedio: 8,488,708.35 -------4 personas
#Costo Promedio: 933,825.26 -------3 personas
