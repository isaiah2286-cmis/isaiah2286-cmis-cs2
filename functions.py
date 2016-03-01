import math
def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def mul(a, b):
	return a * b

def div(a ,b):
	return float(a) / b

def hours_from_seconds(a):
	return a/3600

def area_circle(r):
	return math.pi*r**2

def sphere_volume(r):
	return (r**3)*math.pi*4/3

def avg_volume(a, b):
	return (sphere_volume(a)+sphere_volume(b))/2

def area(a, b, c):
	x = (a + b + c)/2
	return math.sqrt(x*(x-a)*(x-b)*(x-c))

def right_align(a):
	return " "*70+a

def center(a):
	return " "*35+a

def msg_box(a):
	y = "--" + "-" * len(a) + "--"
	return"""
+{}+
|  {}  |
+{}+""".format(y, a, y)

a = add(2, 11)
b = add(3, 1345)
c = sub(2, 124)
d = sub(109357, 395890317)
e = mul(14, 13)
f = mul(35,9535)
g = div(214, 3950)
h = div(109248, 19051)
i = hours_from_seconds(1241515)
j = hours_from_seconds(152355215)
k = area_circle(52)
l = area_circle(43)
m = sphere_volume(63)
n = sphere_volume(12)
o = avg_volume(187, 34)
p = avg_volume(53, 35)
q = area(12, 15, 12)
r = area(45, 23, 53)
s = right_align("noobs")
t = right_align("ezpzz")
u = center("blablabla")
v = center("watever")
print msg_box(str(a))
print msg_box(str(b))
print msg_box(str(c))
print msg_box(str(d))
print msg_box(str(e))
print msg_box(str(f))
print msg_box(str(g))
print msg_box(str(h))
print msg_box(str(i))
print msg_box(str(j))
print msg_box(str(k))
print msg_box(str(l))
print msg_box(str(m))
print msg_box(str(n))
print msg_box(str(o))
print msg_box(str(p))
print msg_box(str(q))
print msg_box(str(r))
print msg_box(str(s))
print msg_box(str(t))
print msg_box(str(u))
print msg_box(str(v))
