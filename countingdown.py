def begining():
    n = int(raw_input("Start counting down from..."))
    countdown(n)
def countdown(n):
    if n <= 0:
        print "gg is done!"
    else:
        print n
        countdown(n-1)
begining()
