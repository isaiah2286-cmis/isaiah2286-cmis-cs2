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

#input
def welcome():
    username = raw_input("Username: ")
    print """Welcome {}! Prepare yourself for the greatest battle of your life!""".format(username)
    no1 = random.randint(0, 10)
    no2 = random.randint(0, 10)
    print "What does ", no1, " X ", no2, "="
    return begining(no1, no2, username)

def begining(no1, no2, username):
    question = no1 * no2
    answer = int(raw_input())
    if answer == question:
        rightorwrong = "right"
    else:
        rightorwrong = "wrong"
    return dealdamage(rightorwrong, username)


#processing


def dealdamage(rightorwrong, username):
    damage = random.random()*4000
    if rightorwrong == "right":
        enermyhp = 4000 - int(damage)
        deltorrecieve = "dealt"
        playerhp = 4000
    else:
        playerhp = 4000 - float(damage)
        deltorrecieve = "received"
        enermyhp = 4000
    return out(playerhp, deltorrecieve, enermyhp, damage, username)
   

#output
def out(playerhp, deltorrecieve, enermyhp, damage, username):
    print """
    You {} {} damage.
    You have {} Hp.    
    Enermy have {} Hp. """.format(deltorrecieve, damage, playerhp, enermyhp)
    if enermyhp <= 0:
        print "Congratulations " + username + " ,you have defeated your enermy!"
    elif playerhp <= 0:
        print "You just got defeated, " + username + " ,what a noob!"
    else:
        return again(username, playerhp, enermyhp)

#continueing the game
def again(username, playerhp, enermyhp):
    no1 = random.randint(0, 10)
    no2 = random.randint(0, 10)
    print "What does ", no1, " X ", no2, "="
    question = no1 * no2
    answer = int(raw_input())
    if answer == question:
        rightorwrong = "right"
    else:
        rightorwrong = "wrong"
    return dealdamageagain(rightorwrong, username, playerhp, enermyhp)

def dealdamageagain(rightorwrong, username, playerhp, enermyhp):
    damage = random.random()*4000
    if rightorwrong == "right":
        enermyhp = enermyhp - int(damage)
        deltorrecieve = "dealt"
    else:
        playerhp = playerhp - float(damage)
        deltorrecieve = "received"
    return out(playerhp, deltorrecieve, enermyhp, damage, username)

welcome()

