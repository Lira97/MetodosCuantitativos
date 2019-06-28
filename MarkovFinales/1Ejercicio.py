#Enrique Lira Martinez A01023351

import numpy as np

NumeroAlumnos = 100

estados_totales = np.zeros((6,6))

Ingreso =        [.1, .8, 0, 0, .1, 0]
NIntermedio =    [0, .1, .85, 0, .05, 0]
NAvanzado =      [0, 0, .15, .8, .05, 0]
Final =         [0, 0, 0, .1, .05, .85]
Desertaron =      [0, 0, 0, 0, 1, 0]
graduandos =       [0, 0, 0, 0, 0, 1]

estudiantes = [NumeroAlumnos, 0, 0, 0, 0, 0]
vector = np.array(estudiantes)

contador = 0
Ingresoo = 0
ultimo = 0

for x in range(6):
	estados_totales[0,x] = Ingreso[x]
	estados_totales[1,x] = NIntermedio[x]
	estados_totales[2,x] = NAvanzado[x]
	estados_totales[3,x] = Final[x]
	estados_totales[4,x] = Desertaron[x]
	estados_totales[5,x] = graduandos[x]

while(True and contador<100):
	if(vector[-1] > 0):
		Ingresoo = contador
	if((round(vector[-1] + vector[-2], 0)) < NumeroAlumnos):
		vector = vector.dot(estados_totales)
		contador += 1
	else:
		ultimo = contador
		print('Numero de {} estudiantes, {} lo que se graduaron y {} no pudieron\n'
			'La probabilidad de graduarse es {}\n'
			'El promedio de tiempo es: {}'
			.format(NumeroAlumnos, int(vector[-1]), int(vector[-2]), round(vector[-1]/NumeroAlumnos, 2), (Ingresoo+ultimo)/2)
			)
		break