#input
def main():
    print """
This  program will ask you for 5 integer or float values.
It will calculate the average of all valus from 0 inclusive to 10 exclusive.
It will print out whether the resulting average is even or odd."""
    no0 = float(raw_input("n0: "))
    if no0 < 0 or no0 >= 10:
        n0 = 0
        zero = 0
        print str(no0) + " is out of range."
    else:
        n0 = no0
        zero = 1
    no1 = float(raw_input("n1: "))
    if no1 < 0 or no1 >= 10:
        n1 = 0
        one = 0
        print str(no1) + " is out of range."
    else:
        n1 = no1
        one = 1
    no2 = float(raw_input("n2: "))
    if no2 < 0 or no2 >= 10:
        n2 = 0
        two = 0
        print str(no2) + " is out of range."
    else:
        n2 = no2
        two = 1
    no3 = float(raw_input("n3: "))
    if no3 < 0 or no3 >= 10:
        n3 = 0
        three = 0
        print str(no3) + " is out of range."
    else:
        n3 = no3
        three = 1
    no4 = float(raw_input("n4: "))
    if no4 < 0 or no4 >= 10:
        n4 = 0
        four = 0
        print str(no4) + " is out of range."
    else:
        n4 = no4
        four = 1
    average = float((n0 +n1 + n2 + n3 + n4)/(zero + one + two + three + four))
    return work(average)

#processing
def work(average):
    intaverage = int(average)
    if intaverage == 0:
        oddoreven = "even"
    elif intaverage == 1:
        oddoreven = "odd"
    elif intaverage == 2:
        oddoreven = "even"
    elif intaverage == 3:
        oddoreven = "odd"
    elif intaverage == 4:
        oddoreven = "even"
    elif intaverage == 5:
        oddoreven = "odd"
    elif intaverage == 6:
        oddoreven = "even"
    elif intaverage == 7:
        oddoreven = "odd"
    elif intaverage == 8:
        oddoreven = "even"
    elif intaverage == 9:
        oddoreven = "odd"
    return out(average, intaverage, oddoreven)

#output
def out(average, intaverage, oddoreven):
    print"""
The average is {}
The integer part of the average is {}.
The integer part is {}.""".format(average, intaverage, oddoreven)

main()

