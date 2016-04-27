def main1():
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
def main2():
    biggestno = 0
    print "The biggest number so far is ", biggestno
    calculation(biggestno)

def calculation(biggestno):
    theno = float(raw_input("Next number: ")





main1()
main2()
