#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a)1000>10 --> True
#b)10 != 10 --> False
#c) "isaiah is sexy" == "isaiah is sexy" --> True
#
#2) What does 'return' do?
# it will use the function when the funtion is called. It is like the output
# so basiclly after the funtion finsih doing everything, if any other funtion want to use the vaiabe that was used in that funtion you have to return it first.
#
#
#3) What are 2 ways indentation is important in python code?
#a)SO you would know when the funtion ends and make it more orgainized
#b)So the computer would understand
#
#

#PART 2: Reading
#Type the values for 9 of the 12 of the variables below.
#
#problem1_a)-36
#problem1_b)-sqrt3
#problem1_c)0
#problem1_d)-5
#
#problem2_a)True
#problem2_b)False
#problem2_c)Flase
#problem2_d)False
#
#problem3_a)0.3
#problem3_b)0.5
#problem3_c)0.5
#problem3_d)0.5
#
#problem4_a)7
#problem4_b)5
#problem4_c)0.125
#problem4_d)5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)


#main/input
def main():
    print "Type in 3 different numbers (decimals are OK!)"
    a = float(raw_input("A: "))
    b = float(raw_input("B: "))
    c = float(raw_input("C: "))
    return work(a, b, c)


#processing
def work(a, b, c):
    if a == b and b == c:
        print "You didn't follow directions!"
    elif a > b and a >c:
        biggestno = a
        return out(biggestno)
    elif b > a and b > c:
        biggestno = b
        return out(biggestno)
    elif c > a and c > b:
        biggestno = c
        return out(biggestno)
    


#output
def out(biggestno):
    print """The largest number was {}""".format(biggestno)

main()
