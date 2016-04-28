def addingno():
    RunningTotal = float(0)
    print "Running total: ", RunningTotal
    calculation(RunningTotal)

def calculation(RunningTotal):    
    addno = raw_input("Next number: ")
    if addno != "":
        print "Running total: ", RunningTotal + float(addno)
        calculation(RunningTotal + float(addno))
    else:
        print "The sum is ", RunningTotal

#----------------------------------------------------------------------------
def biggestno():
    biggestno = 0
    calculation(biggestno)

def calculation(biggestno):
    if biggestno == False:
            print "The biggest number so far is ", biggestno

            calculation(biggestno)
    else: 
        theno = raw_input("Next number: ")
        if theno == "":
            print "The biggest number so far is ", biggestno
        else:
            if biggestno < float(theno):
                biggestno = float(theno)
                print "The biggest number so far is ", biggestno
                calculation(biggestno)
            elif biggestno == 0 and biggestno > float(theno):
                biggestno = float(theno)
                print "The biggest number so far is ", biggestno
                calculation(biggestno)
            else:
                print "The biggest number so far is ", biggestno
                calculation(biggestno)
#----------------------------------------------------------------------------
def smallestno():
    smallestno = 0
    calculation(smallestno)

def calculation(smallestno):
    if smallestno == False:
            print "The smallest number so far is ", smallestno

            calculation(smallestno)
    else: 
        theno = raw_input("Next number: ")
        if theno == "":
            print "The smallest number so far is ", smallestno
        else:
            if smallestno > float(theno):
                smallestno = float(theno)
                print "The smallest number so far is ", smallestno
                calculation(smallestno)
            elif smallestno == 0 and smallestno > float(theno):
                smallestno = float(theno)
                print "The smallest number so far is ", smallestno
                calculation(smallestno)
            else:
                print "The smallest number so far is ", smallestno
                calculation(smallestno)




#addingno()
#biggestno()
smallestno()
