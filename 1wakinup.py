#input
def main():
    print """
This  program will ask you for 5 integer or float values.
It will calculate the average of all valus from 0 inclusive to 10 exclusive.
It will print out whether the resulting average is even or odd."""
    number = 0
    under = 0
    over = 0
    enterno(number, under, over)
def enterno(number, under, over):
    
    no0 = float(raw_input("""n{}: """.format(number)))
    if no0 < 0 or no0 >= 10:
        n0 = 0
        zero = 0
        print str(no0) + " is out of range."
        if number >= 4:
            if under == 0:
                under = 1
                average = over/under
                return work(average)
            else:
                average = over/under
                return work(average)
        else:    
            return enterno(number+1, under, over)
    else:
        n0 = no0
        zero = 1
        if number >= 4:
            average = over/under
            return work(average)
        else:    
            return enterno(number+1, under+1, over+n0)


       

#processing
def work(average):
    intaverage = int(average)
    x = 0
    y = 1
    return oddoreven(intaverage, x)

def oddoreven(average, intaverage, x):
    if intaverage == x:
        oddoreven = "even"
        return oddoreven(average, intaverage, x+2)
    elif intaverage == y:
        oddoreven = "odd"
        return oddoreven(average, intaverage, x+2)
  
    return out(average, intaverage, oddoreven)

#output
def out(average, intaverage, oddoreven):
    print"""
The average is {}
The integer part of the average is {}.
The integer part is {}.""".format(average, intaverage, oddoreven)

main()

