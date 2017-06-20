# Jeremy's reverse polish notation calculator
### Authored 6/20/2017

* Description: The idea behind this calculator is that most operations are centered around the stack. Number inputs would add elements to the stack, operator inputs would pop items off of the stack, apply the operator and add the item back to the stack. This allows us to always maintain the position, as multiple numbers can be on the stack and then operators be applied to those numbers and re-added to the stack.

* Technical Details: I choose a stack due to the implications of the calculator. The last example that demonstrated the ability to add multiple numbers then apply multiple operators fit the characteristics of a stack correctly. Using a language like python also fit the challenge to tackle, as we required something that can accept and return raw input easily. Python is quick to put together simple scripts and also has some built-in testing capabilities that are fairly easy to implement. Python has libraries and the flexibility to add additional features that might be required in the future.

* Trade-offs: I decided to parse single lines with multiple numbers or operators into a different function rather than parse and execute the loop multiple times. This limits single line statements to two different patterns; however as per the examples, it didn't seem neceesary to be able to incorporate more than this format. If the requirements change to actually require single line statements with more than two numbers and 1 operator, it is not difficult to change the program due to the appropriatley structured program. This doesn't fit with the model of using the stack, however it can be easily changed to conform if additional requirements are necessary. 

* How to Run: 
** Calculator: python revpolish.py
** Test Suite: python test.py
** (uses python 2.7, Ctrl-D works on select operating systems)

* Github Code: https://github.com/germy/revpolish
* Challenge Instructions: https://gist.github.com/nilbus/fd0c0c82d6a062d1c1833e0c87622473