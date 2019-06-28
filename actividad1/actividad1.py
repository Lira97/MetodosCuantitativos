#Enrique Lira Martinez A01023351 Caminata aleatoria 
import random
from collections import Counter
from statistics import mode
x=0
l=[[1, 1], [2, 3], [3, 3], [3,3], [4,4]]
lista= []
coord = [0,0]

for j in range(0,49999):
	coord[0]=0
	coord[1]=0
	for i in range(10):
		a=random.randint(0,99)
		if a >=  0 and a <= 24:
			coord[0]=coord[0]+1
		if a >=  25 and a <= 49:
			coord[0]=coord[0]-1
		if a >=  50 and a <= 74:
			coord[1]=coord[1]+1
		if a >=  75 and a <= 99:
			coord[1]=coord[1]-1	
				
	if	coord[0] ==  -2 and coord[1] == 0 or coord[0] ==  2 and coord[1] == 0 or coord[0] ==  0 and coord[1] == 2 or coord[0] ==  0 and coord[1] == -2:
		x=x+1
	if	coord[0] ==  -1 and coord[1] == 1 or coord[0] ==  1 and coord[1] == -1 or coord[0] ==  1 and coord[1] == 1 or coord[0] ==  -1 and coord[1] == -1 or coord[0] == 0 and coord[1] == 0:
		x=x+1
	lista.append((coord[0],coord[1]))
print("La probabilidad de estar en 2 cuadras es de:",x/50000*100,"%")	
print("La cuadra mas comun es:",Counter(lista).most_common(1)[0][0])
print("La probabilidad de la coordenada es de:",Counter(lista).most_common(1)[0][1]/50000*100,"%")
	


