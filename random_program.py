print "please login into your email."
def output(a, b, d, name):
	return """
Hey whats up, {}?
Your email is {}
your password is {}
""".format(name, a, d)

def main():
	a = raw_input("Email: ")
	b = raw_input("password: ")
	c = len(b)
	d = "*"* c
	name = raw_input("Name: ")
	print output(a, b, d, name)

main()
