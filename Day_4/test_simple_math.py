# test_simple_math.py
from simple_math import *
# the name of the testing function should
# also start with test_
def test_simple_math():
	a = 2; b =3; x =4; c =5
	assert simple_add(a, b) == 5
	assert simple_sub(a, b) == -1
	assert simple_mult(a, b) == 6
	assert simple_div(a, b) == 2/3
	assert poly_first(x, a, b) == 14
	assert poly_second(x, a, b, c) == 94