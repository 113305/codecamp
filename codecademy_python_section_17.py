#17.1
my_dict ={
    "Name": "MinSeon",
    "Age": 21,
    "BDFL": True
    }

print my_dict.items()

#17.2
my_dict ={
    "Name": "MinSeon",
    "Age": 21,
    "BDFL": True
    }

print my_dict.keys(),my_dict.values()

#17.3
my_dict ={
    "Name": "MinSeon",
    "Age": 21,
    "BDFL": True
    }

print my_dict.keys(),my_dict.values()

for key in my_dict:
    print key, my_dict[key]

#17.5
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(2,11) if x%2 == 0]

print even_squares

#17.6
cubes_by_four = [ x*x*x for x in range(1, 11) if (x*x*x)%4 == 0]

print cubes_by_four

#17.8
my_list = range(1, 11) # List of numbers 1 - 10

print my_list[::2]

#17.9
my_list = range(1, 11)

backwards = my_list[::-1]

#17.10
to_one_hundred = range(101)

backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

#17.11
to_21 = [ x for x in range(1, 22) ]
odds = to_21 [::2]
middle_third = to_21[len(to_21)/3:(len(to_21)/3)*2:]

#17.13
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x=="Python", languages)

#17.14
squares = [ x**2 for x in range(1,11) ]
print filter(lambda x: x >= 30 and  x<= 70, squares)

#17.15
movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print movies.items()

#17.16
threes_and_fives = [ x for x in range(1, 16) if x%3 ==0 or x%5 ==0]

#17.17
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]

#17.18
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x!='X', garbled)
print message
