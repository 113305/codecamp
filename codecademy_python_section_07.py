#7.2
def spam():
    """Eggs!"""
    print "Eggs!"

spam()

#7.3
def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared

# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.

square(10)

#7.4
def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!

#7.5
def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2

#7.6
def cube(n):
    return n * n * n

def by_three(n):
    if n%3 == 0:
        return cube(n)
    else:
        return False

#7.8
import math
print math.sqrt(25)

#7.9
from math import sqrt

#7.10
from math import *

#7.11
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything

#7.13
maximum = max(1,2,3)

print maximum

#7.14
minimum = min(1,2,3)

print minimum

#7.15
absolute = abs(-42)

print absolute

#7.16
print type(3)
print type(3.14)
print type('spam')

#7.17
def shut_down(s):
    if s=="yes":
        return "Shutting down"
    elif s=="no":
        return "Shutdown aborted"
    else:
        return "Sorry"

#7.18
import math
print sqrt(13689)

#7.19
def distance_from_zero(a):
    if type(a) == int or type(a)==float:
        return abs(a)
    else:
        return "Nope"
