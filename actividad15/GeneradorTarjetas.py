from random import randint

def random_Tarjerta():
	n = randint(10 ** (16 - 1), (10 ** 16) - 1);
	print (str(n));
	return  n;

def luhnAlgoritmo(card_number):
	digits = [int(d) for d in str(card_number)];
	nones = digits[-1::-2];
	pares = digits[-2::-2];
	check = 0;
	check += sum(nones);
	for d in pares:
		check += sum([int(d) for d in str(d * 2)]);
	if (check % 10 == 0):
		return True;
	else:
		return False;

print ('Valid: ' + str(luhnAlgoritmo(random_Tarjerta())));