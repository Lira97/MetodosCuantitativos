#Enrique Lira Martinez A01023351 Tarjetas de credito
import random
import math
from collections import Counter
from statistics import mode
import numpy as np 
import scipy as sp 
import scipy.stats 
import matplotlib.pyplot as plt # importando matplotlib
import seaborn as sns # importando seaborn
comision = 0;
comisionL=[]
creditosL=[]
rand_general = 0;
mujeres = 0;
hombres = 0;
mujer5 = 0;
mujer10 = 0;
mujer15 = 0;
hombre5 = 0;
hombre10 = 0;
hombre15 = 0;
hombre20 = 0;
sumaDesvEst=0
creditosOtorgados=0

def mean_confidence_interval(data, confidence=0.95): 
	a = 1.0*np.array(data) 
	n = len(a) 
	m, se = np.mean(a), scipy.stats.sem(a) 
	h = se * sp.stats.t._ppf((1+confidence)/2., n-1) 
	return m, m-h, m+h
	
for j in range(0,5000):
	valorT=0
	genreal=random.randint(1,100)
	if genreal <= 30:
		genero=random.randint(1,100)
		if genero <= 20:
			tarjeta=random.randint(1,100)
			hombres=hombres+1
			if tarjeta <= 25:
				credito=random.randint(1,100)
				if credito <= 10:
					creditosOtorgados=creditosOtorgados+1
					hombre5=hombre5+1
					creditosL.append(50000)
					comisionL.append(200)
					comision =comision+ 200
				elif credito >  10 and credito <= 50:
					creditosOtorgados=creditosOtorgados+1
					hombre10=hombre10+1
					creditosL.append(100000)
					comisionL.append(400)
					comision =comision+ 400
				elif credito >  50 and credito <= 80:
					creditosOtorgados=creditosOtorgados+1
					hombre15=hombre15+1
					creditosL.append(150000)
					comisionL.append(600)
					comision =comision+ 600
				elif credito >  80 and credito <= 100:
					creditosOtorgados=creditosOtorgados+1
					hombre20=hombre20+1
					creditosL.append(200000)
					comisionL.append(800)
					comision =comision+ 800
		else:
			mujeres=mujeres+1
			tarjeta=random.randint(1,100)
			if tarjeta <= 15:
				credito=random.randint(1,100)
				if credito <= 60:
					creditosOtorgados=creditosOtorgados+1
					mujer5=mujer5+1
					creditosL.append(50000)
					comisionL.append(200)
					comision =comision+ 200
				elif credito >  60 and credito <= 90:
					creditosOtorgados=creditosOtorgados+1
					mujer10=mujer10+1
					creditosL.append(100000)
					comisionL.append(400)
					comision =comision+ 400
				elif credito >  90 and credito <= 100:
					creditosOtorgados=creditosOtorgados+1
					mujer15=mujer15+1
					creditosL.append(150000)
					comisionL.append(600)
					comision =comision+ 600
					
print("\n----------Creditos------------\n")
print("Las creditos serían de :", sum(creditosL))
print("Numero de creditos ", hombres+mujeres)
print("La media en la creditos sería",np.mean(creditosL))
print("La mediana en la creditos sería",np.median(creditosL))
print("La varianza en la creditos sería",np.var(creditosL))
print("La desviacion estandar en la creditos sería",np.std(creditosL))
print("La moda en la creditos sería",mode(creditosL))
print("Intervalos de confianza ",mean_confidence_interval(creditosL))
print("\n----------Comisiones------------\n")
print("Las comisiones serían de :", comision)
print("Numero de comisiones ", hombres+mujeres)
print("La media en la comision sería",np.mean(comisionL))
print("La mediana en la comision sería",np.median(comisionL))
print("La varianza en la comisiones sería",np.var(creditosL))
print("La desviacion estandar en la comision sería",np.std(comisionL))
print("La moda en la comision sería",mode(comisionL))
print("Intervalos de confianza ",mean_confidence_interval(comisionL))
print("\n-----------Creditos por genero -----------\n")
print("Hombres:", hombres ,"Mujeres:", mujeres )
print("Mujeres(5,000 - 10,000 - 15,000):", mujer5,mujer10,mujer15)
print("Hombres(5,000 - 10,000 - 15,000 - 20,000):", hombre5,hombre10,hombre15,hombre20)


sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})

mu, sigma = np.mean(comisionL), np.std(comisionL) # media y desvio estandar

s = np.random.normal(mu, sigma, 5000) #creando muestra de datos
# histograma de distribución normal.
cuenta, cajas, ignorar = plt.hist(s, 20, density=True)
normal = plt.plot(cajas, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (cajas - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()
