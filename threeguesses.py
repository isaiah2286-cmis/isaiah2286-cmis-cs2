import random

def rounds(roundno, score):
    if roundno == 4:
        print "Game over! Your score is ", score
    else:
        count = 1
        theno = int(random.randint(0, 100))
        print "Round ", roundno
        trys(theno, count, roundno, score)

def trys(theno, count, roundno, score):
    theguess = int(raw_input("The number is: "))
    if count == 5:
        print "Tough luck noob, the number is ", theno
        roundno = roundno + 1
        rounds(roundno, score)
    else:
        if theguess == theno:
            print "Good job, the number is exactly ", theno, ", you must be a pro!!"
            roundno = roundno + 1
            score = score + 1
            rounds(roundno, score)
        elif theguess > theno:
            print "Close, but not close enough. The number is lower! Try again!"
            count = count + 1
            trys(theno, count, roundno, score)
        elif theguess < theno:
            print "Close, but not close enough. The number is higher! Try again!"
            count = count + 1
            trys(theno, count, roundno, score)

def main1():
    print "In this game you will have to find out what is the number that the computer generated from 0 to 100. You will have 5 guesses per round and there are total of 3 rounds. Good luck!"
    roundno = 1
    score = 0
    rounds(roundno, score)

def guessing(guess, guessed, different):
    if guessed <= 6:
        print "I would guess the number is ", guess
        highorlow = raw_input("Thats too high(h), too low(l), or is right(r)")
        if highorlow == "h":
            if different <=1:
                different = 1
            else:
                guessed = guessed + 1
                guess = guess - different
                different = different/2
                guessing(guess, guessed, different)
        elif highorlow == "l":
            if different <= 1:
                different = 1
            else:
                guess = guess + different
                different = different/2
                guessed = guessed + 1
                guessing(guess, guessed, different)
        elif highorlow == "r":
            print "ez, this is just too ez!!"
    elif guessed == 6 or guess >= 100 or guess <= 0:
        print "**** omg is too hard, i give up!"

def main2():
    print "OK, I assume that you have already tried my other game named threeguess. This is basiclly the same, the only difference is that you will create the number from 0 to 100 and the computer will guess it. P.S. kill them boyz (gurls as well)!!!"
    guess = 50
    guessed = 1
    different = 25
    guessing(guess, guessed, different)

def main():
    print "Welcome to this guessing game, where you can just play around with the computer"
    gameno = raw_input("If you would want to guess the number, press 1. If you would want the computer to guess the number, press 2. If you would like to play both, press 3.")
    if gameno == "1":
        main1()
    elif gameno == "2":
        main2()
    elif gameno == "3":
        main1()
        main2()
    else:
        print "ERROR, pleace tpye in 1, 2 ,or 3.    "
        main()
main()
#no that the computer can't guess... 0,1,2,6,8, 14,18

