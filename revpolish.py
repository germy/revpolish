class RPN(object):
  
  def __init__(self):
    self.stack = []
    self.OPERATORS = ['+', '-', '/', '*']

   # function prints the help menu
  def h(self):
    print "--------------------help-------------------"
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

  # function prints the initialization text
  def intro(self):
    print "Welcome to Jeremy's reverse polish calculator"
    print "Type h for help"

  # function parses a single lined statement and handles any parsing errors
  def single(self, var):
    arr = var.split(" ")
    summ = None
    try:
      if len(arr) == 2:
        if len(self.stack) == 0:
          summ =  eval(str(0) + " " + arr[1] + " " + arr[0])
        else:
          summ =  eval(str(self.stack.pop()) + " " + arr[1] + " " + arr[0])        
      elif len(arr) == 3:
        summ =  eval(arr[0] + " " + arr[2] + " " + arr[1])
      if isinstance(summ, float) or isinstance(summ, int):
        print float(summ)
        return float(summ)
      else:
        raise
    except:
      print "Error: there was an issue parsing the input"
      print "the calculator state hasn't changed"
      return None

  # function takes in input values and determines what actions accompany
  # those particular actions
  def calc(self, invar):
    try:
      if invar == "h":
        self.h()
      elif invar == "q":
        print "RPN calculator has quit"
        return False
      elif " " in invar:
        self.stack.append(self.single(invar))
      # checks for an operator input
      elif invar in self.OPERATORS:
        if len(self.stack) > 1:
          # removes items off the stack and evaluates them with given operator
          end = self.stack.pop()
          onein = self.stack.pop()
          self.stack.append(eval(str(onein) + " " + invar + " " + str(end)))
          print self.stack[-1]
        else:
          print "Error: the stack doesn't contain enough items to apply"
          print "an operator onto"
      else:
        # simply adds numbers to the stack, if it can't be interpreted then
        # it raises an exception caught by the try except
        self.stack.append(float(invar))
        print self.stack[-1]
    except:
      print "Error: your input was invalid"
      print "the calculator state hasn't changed"
      
  # main function controls the general workflow    
  def main(self):
    self.intro()
    while True:
      invar = raw_input("> ")
      if self.calc(invar) == False:
        break
  

if __name__ == "__main__":
  calc = RPN()
  calc.main()
