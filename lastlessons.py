def countto0(x):
    while x > 0:
        print x
        x -= 1
    while x < 0:
        print x
        x += 1

def gettheno():
    x = int(raw_input("From what number do you want to count to zero?"))
    countto0(x)

#gettheno()

#-------------------------------------------------------------------------------

def countfromxtoy(x, y):
    while x >= y:
        print x
        x -= 1
    while x <= y:
        print x
        x += 1
#countfromxtoy(20, 10)

#-------------------------------------------------------------------------------

def addoddnoto0(x):
    sumofx = 0
    while x >= 0:
        if x % 2 != 0:
            sumofx += x
            x -= 2
        else:
            x -= 1
    while x <= 0:
        if x % 2 != 0:
            sumofx += x
            x += 2
        else:
            x += 1
    print sumofx 

addoddnoto0(10)        


