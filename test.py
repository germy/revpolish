from revpolish import RPN  # The module which contains the call to input
import sys
from cStringIO import StringIO


def test1():

  old_stdout = sys.stdout
  redirected_output = sys.stdout = StringIO()
  rr = RPN()
  rr.calc("5 6 *")
  sys.stdout = old_stdout

  assert '30.0' == redirected_output.getvalue().strip()
  print "test finished"
  
if __name__ == "__main__":
  test1()