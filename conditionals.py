#Write a description of what your script will do first. This description can be written in gedit and used as the basis of your code later. See this example.
#name the file conditionals.py
#2 conditional execution 
#2 alternative execution 
#2 chained conditionals 
#Use raw_input.
#Use good variable names.
#Use type conversion when necessary.
#Define at least 4 functions that do something substantial (not just adding 2 numbers or multiplying). At least 1 must return a boolean value and be used as a part of the flow control. At least one must return an integer or float. At least 1 must return a string. The 4th can do what ever you want.
#Define a main() function to organize the flow of your program. Be sure to #think about the three phases (input, processing, output)
#Use at least 3 different relational operators.
#Use each of the logical operators at least once. 
#Use random.random() and random.randint() at least once each in your script.
#Use str.format() at least once in your script.
#Use """ or ''' strings at least once in your script.
#Write an interesting and/or entertaining story/game.
#Use the same structure we learned about in the simple program assignment.


#The goal of this game is destory the enermy's castle with math
#The game will generation random math questions if you get it right you will deal some amount of damage to the castle, if you did it wrong it will deal some amount of damage to the player.



import random
import oneguess
#input
def begining():
    username = raw_input("Username: ")
    print "Welcome ", username, "! Prepare yourself for the greatest battle of your life!"
	

#processing
def questions():
    question = random.randint(0, )

def damage():
    damage = random.random(0, 500)
    return damage
#output
def score():
    print """
    {} {} {} damage.
    You have {} Hp.    
    Enermy have {} Hp. """.format(uorenermy, deltorrecieve, damage, playerhp, enermyhp)


