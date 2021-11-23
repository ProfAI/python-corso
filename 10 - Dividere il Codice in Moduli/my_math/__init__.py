
def sqrt(n):

	"""
	Calcolo della radice quadrata di un numero

	Positional arguments:
	n : float -- il numero di cui calcolare la radice quadrata
	"""

	return n**(1/2)


def pow(n,p):

	"""
	Calcolo della potenza di un numero
	
	Positional arguments:
	n : float -- la base
	p : float -- la potenza da calcolare

	"""

	return n**p


def factorial(n):

	"""
	Calcolo del fattoriale di un numero

	Positional arguments:
	n : float
	   il numero di cui calcolare il fattoriale
	"""

	fact = 0
	
	for i in range(1,n+1):
		fact = fact*i

	return fact


def abs(n):

	"""
	Calcolo del valore assoluto di un numero

	Positional arguments:
	n : float
	   il numero di cui calcolare il valore assoluto
	"""

	return n if n>=0 else -n