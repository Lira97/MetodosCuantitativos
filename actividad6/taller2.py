#Enrique Lira Martinez A01023351 Taller
import random
import math
from collections import Counter
from statistics import mode
import numpy as np
import scipy as sp
import scipy.stats
import matplotlib.pyplot as plt # importando matplotlib

def mean_confidence_interval(data, confidence):
	a = 1.0*np.array(data)
	n = len(a)
	m, se = np.mean(a), scipy.stats.sem(a)
	h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
	return m, m-h, m+h

n_simulations = 50000
n_cars = 0
type_car = 0
costL = []
costPerDay= []
cost = 0

	#Simulación
for i in range(n_simulations):
	n_cars = 0
	type_car = 0

	prob_car = random.randint(1, 100)
	if (prob_car <= 5):
		n_cars = 3
	if (prob_car > 5 and prob_car <= 20):
		n_cars = 4
	if (prob_car > 20 and prob_car <= 50):
		n_cars = 5
	if (prob_car > 50 and prob_car <= 75):
		n_cars = 6
	if (prob_car > 75 and prob_car <= 90):
		n_cars = 7
	if (prob_car > 90 and prob_car <= 100):
		n_cars = 8
	cost = 0
	for j in range (n_cars):
		prob_type = random.randint(1, 100)
		if (prob_type <= 45):
			type_car = 1
		if (prob_type > 45 and prob_type <= 80):
			type_car = 2
		if (prob_type > 80 and prob_type <= 100):
			type_car = 3

			# Carro chico
		if (type_car == 1):
			prob_service = random.randint(1, 100)
			if (prob_service <= 45):
				cost += 350
				costL.append(350)
			if (prob_service > 45 and prob_service <= 60):
				cost += 1575
				costL.append(1575)
			if (prob_service > 60 and prob_service <= 80):
				cost += 1925
				costL.append(1925)
			if (prob_service > 80 and prob_service <= 90):
				cost += 2540
				costL.append(2540)
			if (prob_service > 90 and prob_service <= 100):
				cost += 700
				costL.append(700)

			# Carro mediano
		if (type_car == 2):
			prob_service = random.randint(1, 100)
			if (prob_service <= 25):
				cost += 550
				costL.append(550)
			if (prob_service > 25 and prob_service <= 50):
				cost += 1975
				costL.append(1975)
			if (prob_service > 50 and prob_service <= 65):
				cost += 2545
				costL.append(2545)
			if (prob_service > 65 and prob_service <= 85):
				cost += 2925
				costL.append(2925)
			if (prob_service > 85 and prob_service <= 100):
				cost += 700
				costL.append(700)
			# Carro grande
		if (type_car == 3):
			prob_service = random.randint(1, 100)
			if (prob_service <= 10):
				cost += 750
				costL.append(750)
			if (prob_service > 10 and prob_service <= 25):
				cost += 2275
				costL.append(2275)
			if (prob_service > 25 and prob_service <= 55):
				cost += 2845
				costL.append(2845)
			if (prob_service > 55 and prob_service <= 95):
				cost += 3415
				costL.append(3415)
			if (prob_service > 95 and prob_service <= 100):
				cost += 700
				costL.append(700)
	costPerDay.append(cost)


print(sum(costPerDay)/50000)
print(len(costPerDay))
print(mean_confidence_interval(costPerDay,.95))
print(mean_confidence_interval(costPerDay,.90))
print(mean_confidence_interval(costPerDay,.85))
print(mean_confidence_interval(costPerDay,.80))
print(mean_confidence_interval(costPerDay,.75))
