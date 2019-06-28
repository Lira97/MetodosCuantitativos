import random
import numpy as np
import simpy

maquinas = 1		

lambda_var = 6
tiempoLlegada = np.random.poisson(lambda_var, 5000)	
proceso_1 = np.random.triangular(2, 3, 4, 5000)	
proceso_2 = np.random.triangular(1, 4, 7, 5000)	

tiempoTotal  = 0 
duracionTotal  = 0
fin = 0 
ocio = 0 

NoTrabaja = np.zeros(5000)
def TiempoEspera(env, maquinaria):
	for i in range(5000):
		llegada = tiempoLlegada[i]		
		pieza = Pieza()		
		yield env.timeout(llegada)
		
		env.process(Piezas(env, 'pieza %d' % i, maquinaria, pieza, i)) 
def Pieza():
	pieza = 0
	prob = random.randint(1, 100)

	if(prob >= 1 and prob <= 40): pieza = 1		
	if(prob >= 41 and prob <= 100): pieza = 2	

	return pieza

def Piezas(env, obj, maquinaria, pieza, i):
	global tiempoTotal
	global fin
	global ocio

	llega = env.now 
	if (i == 0):
		ocio += llega
	if (i > 0 and NoTrabaja[i - 1] == 1):
		ocio += (llega - fin)

	with maquinaria.request() as request: 
		yield request 
		pasa = env.now 
		espera = pasa - llega 
		tiempoTotal = tiempoTotal + espera 
		yield env.process(Atender(obj, pieza, i))
		deja = env.now 
		NoTrabaja[i] = 1	
		fin = deja
def Atender(obj, tipo, i):
	global duracionTotal
	
	if(tipo == 1): tiempo_cortiempoTotal = proceso_1[i] 
	if(tipo == 2): tiempo_cortiempoTotal = proceso_2[i]
	yield env.timeout(tiempo_cortiempoTotal) 

	duracionTotal = duracionTotal + tiempo_cortiempoTotal 

env = simpy.Environment()

print ("Simulación Maquinaria")
maquinaria = simpy.Resource(env, maquinas)	
env.process(TiempoEspera(env, maquinaria))		
env.run()										
t_espera_prom = tiempoTotal / 5000
print ("Espera promedio de Piezas: \t%.2f" % t_espera_prom, "min")
t_uso_prom = (duracionTotal / 5000) / maquinas
print ("Uso promedio de máquina: \t%.2f" % t_uso_prom, "min")
ocio_prom = ocio / 5000				
print("Ocio promedio de máquina: \t%.2f" % ocio_prom, "min")	
