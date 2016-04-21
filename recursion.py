def countup(n):
    if n == 10:
        print "BOOM!!!!!"
    else:
	print n
        countup(n + 1)

def main():
    n = int(raw_input("Start counting from "))
    countup(n)
main()
