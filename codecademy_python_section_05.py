#5.2
bool_one = 17<328
bool_two = 100==(2*50)
bool_three = 19<=19
bool_four = -22 >=-18
bool_five = 99 !=(98+1)

#5.3
bool_one = False
bool_two = False
bool_three =  False
bool_four = True
bool_five = False

#5.4
bool_one = 3 < 5
bool_two = 3>5
bool_three = 1==1
bool_four = 5<4
bool_five = 6<7

#5.6
bool_one = False and False
bool_two = -(-(-(-2))) == -2 and 4 >= 16**0.5
bool_three = 19 % 4 != 300 / 10 / 10 and False
bool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2
bool_five = True and True

#5.7
bool_one = True
bool_two = True
bool_three = False
bool_four = True
bool_five = False

#5.8
bool_one = False
bool_two = True
bool_three = True
bool_four = True
bool_five = False

#5.9
bool_one = 1==3 or not 1==1 and 2==2
bool_two = 1>2 and not 1==1 or 2==2
bool_three = 2==2 and not ( 1>3 or 4>5)
bool_four = not not 1==1 or 4>7 and not 1==1
bool_five = 4>5 or not (1==1 and 2==2)

#5.10
# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"
# Make me true!
bool_two = 1==1 or 2==3
# Make me false!
bool_three = 1==1 and 2==3
# Make me true!
bool_four = not 1==3
# Make me true!
bool_five = not not 1==1

#5.11
response = "Y"

answer = "Left"
if response == "Y":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"

#5.12
def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print using_control_once()
print using_control_again()

#5.13
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:
        return False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return False

#5.14
def greater_less_equal_5(answer):
    if answer >5:
        return 1
    elif answer<5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

#5.15
# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if 1==1 and 2==2:    # Start coding here!
        # Don't forget to indent
        # the code inside this block!
        return True
    elif 3==3 or 4>5:
        # Keep going here.
        # You'll want to add the else statement, too!
        return True
    else:
        return True
