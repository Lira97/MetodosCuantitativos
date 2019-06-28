#Enrique Lira Martinez A01023351 redondeo
import random
import math
from collections import Counter
from statistics import mode
x=0
pago=99.20
lista= []

for j in range(0,49999):
	a=random.randint(0,99)
	if random.randint(0,100) < .2:
		lista.append(math.floor(pago))
	if random.randint(0,100) >= .2:
		lista.append(math.ceil(pago))

print(Counter(lista).most_common(1)[0][1]/50000*100)
	