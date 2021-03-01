import simple_math as sm

def test_add():
	assert sm.simple_add(2, 1) == 3
    
def test_div():
	assert sm.simple_div(10, 2) == 5    

def test_mult():
	assert sm.simple_mult(3, 4) == 12

def test_sub():
	assert sm.simple_sub(3, 1) == 2

def test_poly_first():
	assert sm.poly_first(2, -4, 2) == 0

def test_poly_second():
	assert sm.poly_second(-2, 4, 4, 1) == 0
