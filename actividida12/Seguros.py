#Enrique Lira Martinez A01023351
from scipy.stats import poisson
import random
import numpy as np
import matplotlib.pyplot as plt
def PagoProb():
	probabilidad = random.randint(1, 100)
	if(probabilidad <= 19):
		pagos = 0
	if(probabilidad > 19 and probabilidad <= 25):
		pagos = 5000
	if(probabilidad > 25 and probabilidad <= 40):
		pagos = 10000
	if(probabilidad > 40 and probabilidad <= 60):
		pagos = 15000
	if(probabilidad > 60 and probabilidad <= 72):
		pagos = 20000
	if(probabilidad > 72 and probabilidad <= 80):
		pagos = 30000
	if(probabilidad > 80 and probabilidad <= 86):
		pagos = 40000
	if(probabilidad > 86 and probabilidad <= 91):
		pagos = 50000
	if(probabilidad > 91 and probabilidad <= 95):
		pagos = 60000
	if(probabilidad > 95 and probabilidad <= 98):
		pagos = 70000
	if(probabilidad > 98 and probabilidad <= 99):
		pagos = 80000
	if(probabilidad > 99 and probabilidad <= 100):
		pagos = 100000
	return pagos

def main():
	nOfSimulations = 50000
	array = []
	tempSum = 0
	posionDist = np.random.poisson(3, 50000)
	for i in range(nOfSimulations):#Simulations
		for j in range(posionDist[i]):
			tempSum += PagoProb()
		array.append(tempSum)
		tempSum = 0
	print("El pago diario es de:",np.average(array))
	return np.average(array)


if __name__ == "__main__":
	main()
