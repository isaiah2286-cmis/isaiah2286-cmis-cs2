import math
def add(a, b):
	return a + b
print add(3, 4)
def sub(a, b):
	return a - b
print sub(5, 3)
def mul(a, b):
	return a * b
print mul(4, 4)
def div(a ,b):
	return float(a) / b
print div(2, 3)
def hours_from_seconds(a):
	return a/3600
print hours_from_seconds(86400)
def area_circle(r):
	return math.pi*r**2
print area_circle(5)
def sphere_volume(r):
	return (r**3)*math.pi*4/3
print sphere_volume(5)
def avg_volume(a, b):
	return ((((a/2)**3)*math.pi*4/3)+(((b/2)**3)*math.pi*4/3))/2
print avg_volume(10, 20)
def area(a, b, c):
	x = (a + b + c)/2
	return math.sqrt(x*(x-a)*(x-b)*(x-c))
print area(1, 2, 2.5)
def right_align(a):
	return " "*80+a
print right_align("hello")
def center(a):
	return " "*40+a
print center("hello")
def msg_box(a):
	y = "--" + "-"*len(a) + "--"
	return"""
+{}+
|  {}  |
+{}+""".format(y, a, y)

print msg_box("hello")
print msg_box("I eat cats!")
