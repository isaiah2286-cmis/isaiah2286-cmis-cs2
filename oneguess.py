import random



#input

def getno():
	minimumno = raw_input("What is the minimum number? ")
	maximumno = raw_input("What is the maxium number? ")
	theguess = raw_input("What do you think it is? ")
	theno = random.randint(minimumno, maximumno)
	return output()

#process

def calculation():
    if minimumno > theno:
        return True
    elif minimumno < theno:
    
#output

def output():
    print"""
    The target was {}.
    Your guess was {}.
    That's {} by {}.
    """.format(theno, theguess, underorover, thedifference)
