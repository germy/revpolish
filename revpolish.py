OPERATORS = ['+', '-', '/', '*']


def intro():
    print "Welcome to Jeremy's reverse polish calculator"
    print "Type help for help"

def quit():
    print "RPN has quit"

def calc():
    num1 = 0
    num2 = 0
    op = ""
    while True:
        try:
            invar = raw_input("> ")            
            if invar == "help":
                help()
            elif invar == "q":
                quit()
                break
            elif invar in OPERATORS:
                

            print "you entered " + input_var
        except EOFError:
            quit()
            break
        except:
            print "your input was invalid, the calculator has been cleared"

def main():
    intro()
    calc()

if __name__ == "__main__":
    main()
