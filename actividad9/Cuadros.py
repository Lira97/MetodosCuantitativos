#Enrique Lira Martinez A01023351
from random import randint

profit1 = 0;
profit2 = 0;
profit3 = 0;

for test in range (1, 5001):
	prob = randint(1, 100);
	if (prob <= 60):
		profit1 += 100000;
		prob = randint(1, 100);
		if (prob <= 60):
			profit2 += 200000;
			prob = randint(1, 100);
			if (prob <= 60):
				profit3 += 240000;

print("Mismo día: ", profit1/5000, "\n", 
"Segundo día: ", profit2/5000, "\n", 
"Tercer día: ", profit3/5000, "\n");
#Mismo día:  60360.0 
# Segundo día:  71800.0 
# Tercer día:  51312.0 
