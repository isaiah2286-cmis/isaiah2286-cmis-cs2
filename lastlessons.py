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
    if x > 0:
        while x > 0:
            if x % 2 != 0:
                sumofx += x
            x -= 1
    elif x < 0:
        while x < 0:
            if x % 2 != 0:
                sumofx += 1
        x += 1
    print sumofx
            
#addoddnoto0(-20)        

#-------------------------------------------------------------------------------

def dots(w, h):
    out = ""
    x = 0
    while x < h:
        out += "."
        x += 1
    return out
print dots(15, 10)		
