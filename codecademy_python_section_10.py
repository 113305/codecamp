#10.1
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names:
    print name

#10.2
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print webster[key]

#10.3
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for item in a:
    if item %2 ==0:
        print item

#10.4
# Write your function below!
def fizz_count(x):
    count = 0
    for item in x:
        if item=="fizz":
            count += 1
    return count

fizz_count(["fizz","cat","fizz"])

#10.6
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

#10.7
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

#10.8
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for item in prices:
    print item
    print "price: %s" % prices[item]
    print "stock: %s" % stock[item]

#10.9
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

total = 0

for item in prices:
    total += prices[item] * stock[item]

print total

#10.10
groceries = ["banana", "orange", "apple"]

#10.11
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        total += prices[item]
    return total

#10.12
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item]>0:
            total += prices[item]
            stock[item] -= 1

    return total
