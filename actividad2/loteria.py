#Enrique Lira Martinez A01023351 Loteria
from random import *
import numpy as np
from collections import Counter

iteraciones=0
a = []
b = []
c = []
d = []
e = []
lista = []
ticketGanador= []
ticketGordo= []
for j in range(0,49999):

	numbers = sample(range(1,70), 5)
	o=randint(1,25)
	a.append(numbers[0])
	b.append(numbers[1])
	c.append(numbers[2])
	d.append(numbers[3])
	e.append(numbers[4])
	lista.append(o)
	
print("Estos fueron los numeros que mas se repitieron",Counter(a).most_common(1)[0][0],Counter(b).most_common(1)[0][0],Counter(c).most_common(1)[0][0],Counter(d).most_common(1)[0][0],Counter(e).most_common(1)[0][0])
print("Estos son el numero de veces que se repitieron",Counter(a).most_common(1)[0][1],Counter(b).most_common(1)[0][1],Counter(c).most_common(1)[0][1],Counter(d).most_common(1)[0][1],Counter(e).most_common(1)[0][1])
print("El numero extra se repitio",Counter(lista).most_common(1)[0][1],"veces y fue el numero",Counter(lista).most_common(1)[0][0])
ticketGanador.append(Counter(a).most_common()[0][0])
ticketGanador.append(Counter(b).most_common()[0][0])
ticketGanador.append(Counter(c).most_common()[0][0])
ticketGanador.append(Counter(d).most_common()[0][0])
ticketGanador.append(Counter(e).most_common()[0][0])
ticketGordo.append(Counter(lista).most_common()[0][0])

numeros = sample(range(1,70), 5)
extra = sample(range(1,25), 1)
condicion = False
while (condicion == False):
	if (set(ticketGanador) == set(numeros) and ticketGordo == extra):
		condicion = True
	numeros = sample(range(1,70), 5)
	extra = sample(range(1,25), 1)
	iteraciones=iteraciones+1

print("Se tendrian que comprar",iteraciones,"boletos")
