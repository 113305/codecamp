#2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking or bad user data.
#Challenge: check to make sure the input is a valid number



# This first line is provided for you

hrs = str(input("Enter Hours:"))
hours2 = hrs.split(".")
hours3 = "".join(hours2)
if hours3.isdigit():
    pay = str(input("Enter pay:"))
    pay2 = pay.split(".")
    pay3="".join(pay2)
    if pay3.isdigit():
        h = float(hrs)
        p = float(pay)
        total = h * p
        print(total)
    else:
        print("Pay isn't a valid number.")
else:
    print("Hours isn't valid number.")
