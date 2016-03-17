import random



#input

def getno():
    minimumno = int(raw_input("What is the minimum number? "))
    maximumno = int(raw_input("What is the maxium number? "))
    print """I'm thinking of a number from {} to {}.""".format(minimumno, maximumno)
    theguess = int(raw_input("What do you think it is? "))
    theno = int(random.randint(minimumno, maximumno))
    return calculation(theguess, theno)

#process

def calculation(theguess, theno):
    thedifference = int(abs(theguess - theno))
    if theguess > theno:
        underorover = """That's over by {}""".format(thedifference)
    elif theguess < theno:
        underorover = """That's under by {}""".format(thedifference)
    else:
        underorover = "That's correct! You must be a psychic!!"
    return output(theno, theguess, underorover)
    
#output

def output(theno, theguess, underorover):
    print"""
    The target was {}.
    Your guess was {}.
    {}
    """.format(theno, theguess, underorover)

getno()
