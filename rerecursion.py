def enterno():
    bottom = int(raw_input("Enter the lowest number: "))
    top = int(raw_input("Enter the highest number: "))
    countupbetweenno(bottom, top)
    countdownbetweenno(bottom, top)

def countupbetweenno(bottom, top):
	
    if bottom == top+1:
        print "BOOM!!!!!"
    else:
        print bottom
        countupbetweenno(bottom+1, top) 


def countdownbetweenno(bottom, top):
    if top == bottom-1:
        print "!()*#()!@$*!$@@!)(*$"
    else:
        print top
        countdownbetweenno(bottom, top-1)


enterno()
