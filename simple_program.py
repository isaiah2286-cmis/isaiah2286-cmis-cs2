
#output
def output(un, a, b, c):
	out = """Welcome {}, thank you for choosing our company. Enjoy.
This free trail will allow you to find things about yourself...
You are around {} days old.
Your are {} cm away from being an average NBA player.
Your are 1/{} of earth's mass.
""" .format(un, a, b, c)

	return out

#input
def main():
	
    fn = raw_input("First Name: ")
    ln = raw_input("Last Name: ")
    un = raw_input("Username: ")
    p = raw_input("Password: ")
    age = raw_input("Age: ")
    h = raw_input("Your height in centimeter: ")
    w = raw_input("Your weight in kilogram: ")
    e = raw_input("Email address: ")
    pa = raw_input("Password: ")
    a = int(age) * 365
    b = 180 - int(h)
    c = int(w) / 5.972 * (10**24)
    out = output(un, a, b, c)
	
    print out

main()
