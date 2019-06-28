#Enrique Lira Martinez A01023351
import numpy as np

NumeroArticulos = 1000 
costo = 0
completados = 0

MatrizEstados = np.zeros((8,8))
MaquinaA =      [0, .93, 0, 0, 0, 0, .07, 0]
InspectorA =    [.04, 0, .94, 0, .0, 0, .02, 0]
MaquinaB =      [0, 0, 0, .95, 0, 0, .05, 0]
InspectorB =    [0, 0, .03, 0, .96, 0, .01, 0]
MaquinaC =      [0, 0, 0, 0, 0, .97, .03, 0]
inspectorC =    [0, 0, 0, 0, .01, 0, .01, .98]
desechos =      [0, 0, 0, 0, 0, 0, 1, 0]
empaque =       [0, 0, 0, 0, 0, 0, 0, 1]

Articulos = [NumeroArticulos, 0, 0, 0, 19, 0, 0, 0]
vector = np.array(Articulos)

TiempoOperacion = [3, .25, 2.5, .25, 1.5, .25, 0, .1]
costoOperacion = [10, 10, 10, 10, 12, 10, 0, 8]
gastos = []

for h, c in zip(TiempoOperacion, costoOperacion):
	gastos.append(h*c)

for x in range(8):
	MatrizEstados[0,x] = MaquinaA[x]
	MatrizEstados[1,x] = InspectorA[x]
	MatrizEstados[2,x] = MaquinaB[x]
	MatrizEstados[3,x] = InspectorB[x]
	MatrizEstados[4,x] = MaquinaC[x]
	MatrizEstados[5,x] = inspectorC[x]
	MatrizEstados[6,x] = desechos[x]
	MatrizEstados[7,x] = empaque[x]

c1 = 0

while(int(vector[-1] < NumeroArticulos)):
	if(int(vector[-1]) < NumeroArticulos and round(vector[-1] + vector[-2], 0) >= NumeroArticulos):
		vector[0] += 1
	costo += (vector.dot(gastos) - (c1 * gastos[-1]))
	c1 = int(vector[-1])
	vector = vector.dot(MatrizEstados)

print('Numero de articulos necesarios {} para {}\n''El costo seria de: ${}'.format(int(vector[-1] + vector[-2]), NumeroArticulos, round(costo,2)))