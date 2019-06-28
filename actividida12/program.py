import numpy as np
import random
import multiprocessing

def Cost():
	probability = random.randint(1, 100)
	if probability <= 19:
		return 0
	elif probability > 19 and probability <= 25:
		return 5000
	elif probability > 25 and probability <= 40:
		return 10000
	elif probability > 40 and probability <= 60:#.20
		return 15000
	elif probability > 60 and probability <= 72:#.12
		return 20000
	elif probability > 72 and probability <= 80:#.08
		return 30000
	elif probability > 80 and probability <= 86:#.06
		return 40000
	elif probability > 86 and probability <= 91:#.05
		return 50000
	elif probability > 91 and probability <= 95:#.04
		return 60000
	elif probability > 95 and probability <= 98:#.03
		return 70000
	elif probability == 99:#.01
		return 80000
	elif probability == 100:#.01
		return 100000

def main(x):
	nOfSimulations = 50000
	array = []
	tempSum = 0
	posionDist = np.random.poisson(3, 50000)
	for i in range(nOfSimulations):#Simulations
		for j in range(posionDist[i]):
			tempSum += Cost()
		array.append(tempSum)
		tempSum = 0
	return np.average(array)
	

pool = multiprocessing.Pool()
winnersList = pool.map(main, range(100))
pool.close()
print("El pago diario es de: " + str(np.average(winnersList)) + ".")
