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

def q():
    print "RPN has quit"

def single(var, num1, num2):
    arr = var.split(" ")
    summ = None
    try:
        if len(arr) == 2:
            summ =  eval(str(num1) + " " + arr[1] + " " + arr[0])
        elif len(arr) == 3:
            summ =  eval(arr[0] + " " + arr[2] + " " + arr[1])
        if isinstance(summ, float) or isinstance(summ, int):
            return float(summ)
    except:
        print "There was an issue pasing"
        return None

def calc():
    num1 = None
    num2 = None
    while True:
        try:
            invar = raw_input("> ")            
            if invar == "h":
                h()
            elif invar == "q":
                q()
                break
            elif " " in invar:
                num1 = single(var, num1, num2)
                num2 = None
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
            q()
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
