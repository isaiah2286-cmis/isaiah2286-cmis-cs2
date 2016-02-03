#this is the variable for my name
myname = "Isaiah Kwong"
#this is the variable for my age
myage = 18 + (12+29+30) / 365.0
#this is the variable for my height
myheightinm = 1.74
#this is the variable for of one side of the square
sq1side = 3
#this is the variable for length of the rectangle
lengthrec = 10
#this is the variable for the height of the rectangle
heightrec = 20
#this is the variable for my age in month
myageinmonth = myage * 12
#this is the variable for life expectancy in hong kong
lifeexpectancy = 82.44
#this is the variable for the days that i can still live
mydaysleft = lifeexpectancy - myage
#this is the variable for the unit converter from ft to m
mtoft = 3.28084
#this is the variable for my height in foot
myheightinft = myheightinm * mtoft
#this is the variable for the average height in hong kong
averageheight = 1.70
#this is the variable for this is the height different between be and people from my home country
heightdifferent = myheightinm - averageheight
#this is the variable for finding the area of the square
areaofsq = sq1side ** 2
#this is the variable for half of the volume of the rectangluar prism
halfvolume = (lengthrec ** 2 * heightrec) / 2.0
#this is the variable for one ninth of the area of the prism
oneovernine = (halfvolume / (heightrec/2))/9
#this is actually the main point of this assignment, the variable we used shows up now
print	"Hello world, my name is " + str(myname) + "and I am " + str( myage) + "years old. Compare to average age in Hong Kong, I still have" + str(mydaysleft) + " years left to live. I am " + str(myheightinm) + "M which means I am " + str(myheightinft) + "ft tall. I want to be at least 6 foot tall tho. T^T" 
# this is so much essier than the last one becuase you just have to add commar and not plus sign and "str"
print "1. Bill is planning to build a square shaped swimming pool. Each side of the simming pool is" , sq1side , "M long, find the area. ~~~~~ The area of the swimming pool is" , areaofsq , "M^2. 2. A rectangular prism has height of" , heightrec , "M and a length of" , lengthrec , "find half of the volume of the prism. ~~~~ Half of the volume of the prism is" , halfvolume
print ";)" *10000

