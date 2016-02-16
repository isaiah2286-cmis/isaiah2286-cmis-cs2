def mul(a, b):
	c= a*b
	return c

def output(name, a, b, c):
	return """
Hey whats up, {}?
This is a multiplication calculator that can multipy any two numbers!
{} x {} = {}
""".format(name, a, b, c)

def main():
	name = raw_input("Name: ")
	a = raw_input("First number: ")
	b = raw_input("Second number: ")
	c = mul(int(a), int(b))
	print output(name, a, b, c)

main()

