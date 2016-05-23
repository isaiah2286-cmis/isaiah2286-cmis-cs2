
#Section 1: Terminology
# 1) What is a recursive function?
#	A function that will call itself inside its own defination
#
#
# 2) What happens if there is no base case defined in a recursive function?
#   Your program will run forever or u will just have the message "RuntimeError: maximum recursion depth exceeded while getting the str of an object" so it does not work

#
#
# 3) What is the first thing to consider when designing a recursive function?
#We have to know what does it do. what is or base case
#
#
# 4) How do we put data into a function call?
#   we can use raw_input
#
# 
# 5) How do we get data out of a function call?
#   we can return it or call it or just print it
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 =2
#a2 =6
#a3 =-1

#b1 =2
#b2 =0
#b3 =1

#c1 =-2
#c2 =4
#c3 =5

#d1 =6
#d2 =7
#d3 =5

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


#input and this is basicly all i need, it will have find all the odd number and the adverage of it
def enterno(n, count):
    addno = raw_input("Enter number here: ")
#to find the average of odd number
    if addno == "":
        x = n/count
        print x
    else:    
#to find the odd number
        if float(addno) % 2 == 0:
            enterno(n, count)
        else:
#to find the sum of odd number
            n = n + float(addno)
            count = count + 1
            enterno(n, count)



def main():
    n = 0
    count = 0
    enterno(n, count)

#main()
def function1(x, n):
    if n <=0:
        return x
    else:
        return 1 + function1(x, n-1)
def function2(a, b):
    if a <= 0:
        return 1 + function2(a+1, b**a)
    else:
        return b

def this():
    print function2(-2, -2)
this()
