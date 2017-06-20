from revpolish import RPN  # The module which contains the call to input
import sys
from cStringIO import StringIO

# README
# the calctester function captures the stdout for python to determin
# what was printed after the calculator was run


def calctester(expected, eq, instance):
  old_stdout = sys.stdout
  redirected_output = sys.stdout = StringIO()
  instance.calc(eq)
  sys.stdout = old_stdout
  value = redirected_output.getvalue().strip()
  if expected == value:
    print "+ passed: " + str(eq) + " = " + str(value)
  elif (("Error" in value) or ("help" in value) or ("quit" in value)) \
    and expected in value:
    print "+ passed: expected output occured"
  else:
    print "- failed: " + str(eq) + " = " + str(value)

def test1():
  rr = RPN()
  calctester('30.0', '5 6 *', rr)
  calctester('36.0', '6 +', rr)
  calctester('34.0', '2 -', rr)
  calctester('17.0', '2 /', rr)
  calctester('6.0', '6', rr)
  calctester('23.0', '+', rr)
  calctester('10.6', '10.6', rr)
  calctester('33.6', '+', rr)
  calctester('3.36', '10 /', rr)
  calctester('2.0', '2', rr)
  calctester('6.72', '*', rr)
  calctester('6.78', '6.78', rr)
  calctester('4.0', '4', rr)
  calctester('5.0', '5.0', rr)
  calctester('9.0', '+', rr)
  calctester('15.78', '+', rr)
  print "test1 finished"
  print ""
  print "--------------"
  print ""
  
def test2():
  rr = RPN()
  calctester('parsing', '5 6 * 6', rr)
  calctester('operator', '*', rr)
  calctester('30.0', '5 6 *', rr)
  calctester('5.0', '5.0', rr)
  calctester('5.0', '5.0', rr)
  calctester('25.0', '*', rr)
  calctester('30.0', '5 +', rr)
  print "test2 finished"
  print ""
  print "--------------"
  print ""
  
def test3():
  rr = RPN()
  calctester('5.0', '5 +', rr)
  print "test3 finished"
  print ""
  print "--------------"
  print ""
  
def test4():
  rr = RPN()
  calctester('-5.0', '5 -', rr)
  print "test4 finished"
  print ""
  print "--------------"
  print ""  
  
def test5():
  rr = RPN()
  calctester('13.0', '5 8 +', rr)
  calctester('0.0', '13 -', rr)
  print "test5 finished"
  print ""
  print "--------------"
  print ""    

def test6():
  rr = RPN()
  calctester('5.0', '5', rr)
  calctester('9.0', '9', rr)
  calctester('1.0', '1', rr)
  calctester('8.0', '-', rr)
  calctester('0.625', '/', rr)
  print "test6 finished"
  print ""
  print "--------------"
  print ""  
  
def test7():
  rr = RPN()
  calctester('5.0', '5', rr)
  calctester('8.0', '8', rr)
  calctester('13.0', '+', rr)
  print "test7 finished"
  print ""
  print "--------------"
  print ""    
  
def test8():
  rr = RPN()
  calctester('13.0', '5 8 +', rr)
  calctester('0.0', '13 -', rr)
  print "test8 finished"
  print ""
  print "--------------"
  print ""     
  
def test9():
  rr = RPN()
  calctester('-3.0', '-3', rr)
  calctester('-2.0', '-2', rr)
  calctester('6.0', '*', rr)
  calctester('5.0', '5', rr)
  calctester('11.0', '+', rr)
  print "test9 finished"
  print ""
  print "--------------"
  print ""    
    
def test10():
  rr = RPN()
  calctester('invalid', 'geagae-3', rr)
  calctester('help', 'h', rr)
  calctester('quit', 'q', rr)
  print "test10 finished"
  print ""
  print "--------------"
  print ""    
      
  
if __name__ == "__main__":
  test1()
  test2()
  test3()
  test4()
  test5()
  test6()
  test7()
  test8()
  test9()
  test10()