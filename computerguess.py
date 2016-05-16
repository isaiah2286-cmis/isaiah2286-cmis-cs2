def guessing(guess, guessed, different):
    print "I would guess the number is ", guess
    highorlow = raw_input("Thats too high(h), too low(l), or is right(r)")
    if guessed <= 6:
        if highorlow == "h":
            guessed = guessed + 1
            guess = guess - different
            different = different/2
            guessing(guess, guessed, different)
        elif highorlow == "l":
            guess = guess + different
            different = different/2
            guessed = guessed + 1
            guessing(guess, guessed, different)
        elif highorlow == "r":
            print "ez, this is just too ez!!"
    elif guessed >= 6 or guess >= 100 or guess <= 0:
        print "**** omg is too hard, i give up!"

def main():
    print "OK, I assume that you have already tried my other game named threeguess. This is basiclly the same, the only difference is that you will create the number from 0 to 100 and the computer will guess it. P.S. kill them boyz (gurls as well)!!!"
    
    guess = 50
    guessed = 1
    different = 25
    guessing(guess, guessed, different)

def begin():
    n = 1
    compguess = 50
    different = 25
    count = 1
    findthemissing(n, compguess, different, count)

def findthemissing(n, compguess, different, count):
    if n == 101:
        print "stop"
    else:
        if count == 6:
            compguess = 50
            different = 25
            count = 1 
            findthemissing(n+1, compguess, different, count)
        else:
            if n <= compguess:
                compguess = compguess - different
                different = different/2
                count = count + 1
                findthemissing(n, compguess, different, count)
            elif n >= compguess:
                compguess= compguess + different
                different = different/2
                count = count +1
                findthemissing(n, compguess, different, count)
    missin(n, compguess)
def missin(n, compguess):
    if compguess == n:
        print n
    

begin()









#main()
