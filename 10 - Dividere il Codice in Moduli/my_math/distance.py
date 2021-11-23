from . import sqrt, pow, abs


def euclidean(a, b):
	return sqrt( pow(b[0]-a[0], 2) + pow(b[1]-a[1], 2) )


def manhattan(a, b):
	return abs(b[0]-a[0]) + abs(b[0]-a[0])