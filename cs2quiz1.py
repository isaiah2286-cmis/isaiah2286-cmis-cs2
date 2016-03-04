#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# It assigns the value of its right variable to its left value, for example, if you want "a" to represent "asdjf;oiwa;oifjqgijaqoijgj;" you can do "a = asdjf;oiwa;oifjqgijaqoijgj;"
#It also mean that you can use it to put a value into a variable

#2 3pts) Write a technical definition for 'function'
#A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing
#A function is a named sequence of statements that performs a computation.

#3 1pt) What does the keyword "return" do?
#It gives the output of the funtion

#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: interger: 124124551, 141241241
#	2:float: 141421.15214, 12414124.463646
#	3:string: "adflkjafdlkjafd", "akdflnsdflknaf"
#	4:tuple: "asdkfjlafsjafs", 35136516136------ X  -1
#	5:boolean: True, False
#

#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#funtion definition is defining a funtion- def blablabla():
						#return blabla + watever
#function call is using a funtion later on- blablabla("stuffhere", "stuffthere")
#
#

#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:Plannig-  you have to have an idea that what you will be doing and what the program suppose to do-------X -1
#	2:Programing- you actually have to start putting stuff in and create a program------- X -1
#	3:Debugging: as you creating you program, you have to keep debugging your program to see what you've done wrong and fix it.--------X -1
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi
import math
#1 pt for header line
#3 pt for correct formula
#1 pt for return value
#1 pt for parameter name
#1 pt for function name
def diameter(a):
	return math.sqrt(a/math.pi)

#1pt for header line
#1pt for parameter names
#1pt for return value
#1pt for correct output format
#3pt for correct use of format function
def output(d, e, f, g):
	return """
Circle  Diameter
c1      {}
c2      {}
c3      {}
TOTALS  {}
""".format(d, e, f, g)

#1pt header line
#1pt getting input
#1pt converting input
#1pt for calling output function
#2pt for correct diameter formula ------X -1
#1pt for variable names-----X -1
def main():
	a = float(raw_input("Area of circle 1: "))
	b = float(raw_input("Area of circle 2: "))
	c = float(raw_input("Area of circle 3: "))
	d = diameter(a)
	e = diameter(b)
	f = diameter(c)
	g = d + e + f
	print output(d, e, f, g)
#1pt for calling main

main()
#1pt explanatory comments----- X -1
#1pt code format

