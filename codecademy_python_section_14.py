#14.1
count = 0

if count < 5:
    print "Hello, I am an if statement and count is", count

while count < 10:
    print "Hello, I am a while and count is", count
    count += 1

#14.3
num = 1

while num<11:  # Fill in the condition
    print num ** 2
    num += 1

#14.4
choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

#14.5
count = 0

while count < 10:
    print count
    count += 1

#14.8
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if random_number==guess:
        print "You win!"
        break
    guesses_left -= 1
else:
    print "You lose"

#14.9
print "Counting..."

for i in range(20):
    print i

#14.10
hobbies = []

for i in range(3):
    hobby = raw_input()
    hobbies.append(hobby)

#14.11
thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# Your code here!
for c in word:
    print c

#14.12
phrase = "A bird in the hand..."

for char in phrase:
    if char == 'A' or char == 'a':
        print 'X',
    else:
        print char,

#14.13
numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num**2

#14.14
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    print key, d[key]

#14.15
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item

#14.16
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    print max(a,b)

#14.17
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)

    print 'A', f
else:
    print 'A fine selection of fruits!'

#14.18
for i in range(2):
    print "hi"
else:
    print "hello"
