#Enrique Lira Martinez A01023351

import numpy as np
import random

Inicial = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
Final = np.array([[.3, .55, 0], [0, .2, .08], [0, 0, .19]])
Result = np.array([[.05, .1, 0, 0, 0, 0], [.02, 0, .2, .5, 0, 0], [.01, 0, 0, 0, .6, .2]])
Matrix = np.linalg.inv(np.subtract(Inicial, Final))
FResult = np.matmul(Matrix, Result)
print("Probabilidad de que muera es de : {}".format(round(FResult[0][0],2)))
ganancia = 0
for i in range(1000):
	rand2 = random.random()
	if rand2 <= FResult[0][1]:
		ganancia += 2000
	elif FResult[0][1] < rand2 <= FResult[0][2]:
		ganancia += 3000
	elif FResult[0][2] < rand2 <= FResult[0][3]:
		ganancia += 5000
	elif FResult[0][3] < rand2 <= FResult[0][4]:
		ganancia += 10000
	elif FResult[0][4] < rand2 <= FResult[0][5]:
		ganancia += 20000
print("La ganancia promedio es de {}".format(ganancia/1000))