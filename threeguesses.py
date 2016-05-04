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

def main():
    print "In this game you will have to find out what is the number that the computer generated from 0 to 100. You will have 5 guesses per round and there are total of 3 rounds. Good luck!"
    roundno = 1
    score = 0
    rounds(roundno, score)

main()
