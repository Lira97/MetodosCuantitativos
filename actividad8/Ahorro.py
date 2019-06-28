#Nombre: Enrique Lira Martinez A01023351
import random
import numpy as np

edad = 21
retiro = 65
esperanza_vida = 85
gasto=[]


def Gastos(prob1, prob2, gasto1, gasto2, gasto3):
	mensual = 0
	total = 0
	for i in range(12):
		prob = random.randint(1, 100)
		if (prob >= 1) and (prob <= prob1): 
			mensual = gasto1
		if (prob >= prob1 ) and (prob <= prob2): 
			mensual = gasto2
		if (prob >= prob2) and (prob <= 100): 
			mensual = gasto3
		total += mensual

	return total / 12


def Retiro(edad, retiro, esperanza_vida, salario):

	pension = esperanza_vida - retiro
	años_retiro = retiro - edad
	print("Salario total es:", salario)
	print("Tu edad es: ", edad)
	print("Edad de retiro: ", retiro)
	print("Años faltantes: ", años_retiro)
	print("Esperanza de vida: ", esperanza_vida)
	ahorro = ((salario * 12) * pension) / años_retiro
	ahorro = ahorro / 12
	porcentaje_salario = ((ahorro * 100)) / salario
	print("Necesitas comenzar a ahorrar el ", porcentaje_salario, "% de tu salario")
	
def main():
	gasto.append(Gastos(50, 80, 15000, 13000, 10000))	# Renta 
	gasto.append(Gastos(50, 80, 7500, 6000, 5000))		# Alimento
	gasto.append(Gastos(60, 70, 4000, 3500, 3000))		# Servicios(Luz,agua,iternet)
	gasto.append(Gastos(40, 80, 3700, 2600, 2800))		# Carros
	gasto.append(Gastos(60, 70, 3700, 2200, 1200))		# Educacion Basica
	gasto.append(Gastos(70, 80, 2000, 1500, 1000))		# Imprevisto
	gasto.append(Gastos(30, 70, 3100, 2700, 2120))		# Diversion

	Retiro(edad, retiro, esperanza_vida, sum(gasto))

if __name__ == "__main__":
	main()
