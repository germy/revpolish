OPERATORS = ['+', '-', '/', '*']

def h():
    print "This is a reverse polish noation calculator"
    print "valid inputs are float numbers and operators"
    print "to quit type 'q' or Ctrl-D"
    print "the input takes numbers then operators, eg:"
    print "> 5"
    print "5.0"
    print "> 8"
    print "8.0"
    print " > +"
    print "13.0"
    print "-------"
    print "> 5 6 *"
    print "30.0"

def intro():
    print "Welcome to Jeremy's reverse polish calculator"
    print "Type h for help"

def quit():
    print "RPN has quit"

def calc():
    num1 = None
    num2 = None
    while True:
        try:
            invar = raw_input("> ")            
            if invar == "h":
                h()
            elif invar == "q":
                quit()
                break
            elif invar in OPERATORS:
                if isinstance(num1, float) and isinstance(num2, float):
                    num1 = eval(str(num1) + " " + invar + " " + str(num2))
                    num2 = None
                    print num1
                else:
                    print "both numbers are not set, operator has not been applied"
            else:
                try:
                    if num1 == None:
                        num1 = float(invar)
                        print num1
                    elif num2 == None:
                        num2 = float(invar)
                        print num2
                    else:
                        print "an unknown error occurred"
                except:
                    print "input entered is not a valid integer or float value"
        except EOFError:
            quit()
            break
        except:
            num1 = None
            num2 = None
            print "your input was invalid, the calculator has been cleared"

def main():
    intro()
    calc()

if __name__ == "__main__":
    main()
