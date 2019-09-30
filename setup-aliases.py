import math
import numpy as np

PI = math.pi
cross = np.cross
dot = np.dot
length = np.linalg.norm

def vec(*elements):
	return np.array(elements)

def vecn(n, *elements):
	if len(elements) == 0:
		return np.zeros(n)
	if len(elements) == 1:
		return np.repeat(elements[0], n)
	return np.array(elements[0:n])


def vec2(*elements):
	return vecn(2, *elements)

def vec3(*elements):
	return vecn(3, *elements)

def vec4(*elements):
	return vecn(4, *elements)

def cos(degrees):
	return math.cos(degrees / 180 * math.pi)

def sin(degrees):
	return math.sin(degrees / 180 * math.pi)

def tan(degrees):
	return math.tan(degrees / 180 * math.pi)

def acos(a):
	return math.acos(a) / math.pi * 180

def asin(a):
	return math.asin(a) / math.pi * 180

def atan(a):
	return math.atan(a) / math.pi * 180
