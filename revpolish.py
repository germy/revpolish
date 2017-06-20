import atexit

class RPN(object):
  
  def __init__(self):
    self.num1 = None
    self.num2 = None
    self.OPERATORS = ['+', '-', '/', '*']

    
  def h(self):
    print "-------------------------------------------"
    print "This is a reverse polish noation calculator"
    print "valid inputs are float numbers and operators"
    print "to quit type 'q' or Ctrl-D (OS dependent)"
    print "the input takes numbers then operators, eg:"
    print "> 5"
    print "5.0"
    print "> 8"
    print "8.0"
    print " > +"
    print "13.0"
    print "-------------------------------------------"
    print "> 5 6 *"
    print "30.0"
    print "-------------------------------------------"

  def intro(self):
    print "Welcome to Jeremy's reverse polish calculator"
    print "Type h for help"

  def q(self):
    print "RPN calculator has quit"

  def single(self, var):
    arr = var.split(" ")
    summ = None
    try:
      if len(arr) == 2:
        if self.num1 == None:
          summ =  eval(str(0) + " " + arr[1] + " " + arr[0])
        else:
          summ =  eval(str(self.num1) + " " + arr[1] + " " + arr[0])        
      elif len(arr) == 3:
        summ =  eval(arr[0] + " " + arr[2] + " " + arr[1])
      if isinstance(summ, float) or isinstance(summ, int):
        print float(summ)
        return float(summ)
    except:
      print "There was an issue pasing the input, the calculator will reset"
      return None

  def calc(self):
    while True:
      try:
        invar = raw_input("> ")
        if invar == "h":
          self.h()
        elif invar == "q":
          raise EOFError
        elif " " in invar:
          self.num1 = self.single(invar)
          self.num2 = None
        elif invar in self.OPERATORS:
          if isinstance(self.num1, float) and isinstance(self.num2, float):
            self.num1 = eval(str(self.num1) + " " + invar + " " + str(self.num2))
            self.num2 = None
            print self.num1
          else:
            print "both numbers are not set, operator has not been applied"
        else:
          if self.num1 == None:
            self.num1 = float(invar)
            print self.num1
          elif self.num2 == None:
            self.num2 = float(invar)
            print self.num2
          else:
            print "an unknown error occurred"
            print "you may have entereed too many numbers in sequence"
            print "the calculator will reset"
            raise
      except EOFError:
        self.q()
        break
      except:
        self.num1 = None
        self.num2 = None
        print "your input was invalid, the calculator has been cleared"

  def main(self):
    self.intro()
    self.calc()

if __name__ == "__main__":
  calc = RPN()
  calc.main()
