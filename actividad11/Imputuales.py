#Enrique Lira Martinez A01023351
import random

def main():
	nSimulaciones = 5000
	contador = 0
	for i in range(nSimulaciones):
		probabilidadEl = random.randint(1, 60)
		probabilidadElla = random.randint(1, 60)
		if(probabilidadElla >=  probabilidadEl):
			dif = probabilidadElla - probabilidadEl
			if (dif <= 20):
				contador += 1
		else:
			dif = probabilidadEl - probabilidadElla
			if (dif <= 15):
				contador += 1
	promedio = contador/nSimulaciones
	print("La probabilidad de que se encuentren es del",promedio*100,"%")
if __name__ == "__main__":
	main()
