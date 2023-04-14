# A Closure is a function object that remembers values 
# in enclosing scopes even if they are not present in memory.
#  Let us get to it step by step

# In python variables from a higher scopes aren't modified 
# outside nested code, To modify them it is used the keyword
# ! nonlocal

def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)


# Read only behavior example of a pass variable to nested code

def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()

# ADVANTAGE : Closures can avoid use of global variables
# and provides some form of data hiding.(Eg. When there
# are few methods in a class, use closures instead).

# Also, Decorators in Python make extensive use of closures.


#! Exercise

def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))