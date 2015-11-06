#12.1
n = [1, 3, 5]

# Add your code below
print n[1]

#12.2
n = [1, 3, 5]
# Do your multiplication here
n[1] = n[1]*5
print n

#12.3
n = [1, 3, 5]
# Remove the first item in the list here
n.pop(0)
print n

#12.4
number = 5

def my_function(x):
    return x * 3

print my_function(number)

#12.5
m = 5
n = 13
# Add add_function here!
def add_function(x, y):
    return x + y

print add_function(m, n)

#12.6
m = 5
n = 13
# Add add_function here!
def add_function(x, y):
    return x + y

print add_function(m, n)

#12.7
n = "Hello"
# Your function here!
def string_function(s):
    return s + 'world'


print string_function(n)

#12.9
def list_function(x):
    return x[1]

n = [3, 5, 7]
print list_function(n)

#12.10
def list_function(x):
    x[1] = x[1] + 3
    return x

n = [3, 5, 7]
print list_function(n)

#12.11
n = [3, 5, 7]
# Add your function here
def list_extender(lst):
    lst.append(9)
    return lst


print list_extender(n)

#12.12
n = [3, 5, 7]
def print_list(x):
    for i in range(0, len(x)):
        print x[i]

print_list(n)

#12.13
n = [3, 5, 7]

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print double_list(n)

#12.14
def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3)) # Add your range between the parentheses!

#12.15
n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    return result

#12.16
n = ["Michael", "Lieberman"]
def join_strings(words):
    result = ""
    for i in range(len(words)):
        result += words[i]
    return result

print join_strings(n)

#12.17
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x, y):
    return x + y


print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

#12.18
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
    results= []
    for numbers in lists:
        for number in numbers:
            results.append(number)
    return results

print flatten(n)
