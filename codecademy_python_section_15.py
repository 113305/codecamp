#15.2
def is_even(x):
    if x%2==0:
        return True
    else:
        return False

#15.3
def is_int(x):
    if x==int(x):
        return True
    else:
        return False

#15.4
def digit_sum(n):
    sum = 0
    while n>=10:
        sum += n%10
        n = int(n/10)
    sum +=n
    return sum

#15.5
def factorial(x):
    fact = 0
    if x>1:
       fact += x*factorial(x-1)
    else:
        fact = 1
    return fact

#15.6
def is_prime(x):
    if x>=2:
        for i in range(2,x+1):
            if x%i==0:
                if x!=i:
                    return False
                    break
                elif x==i:
                    return True
    else:
        return False

#15.7
def reverse(text):
    reverse = ''
    j = len(text)-1

    while j>=0:
        reverse += text[j]
        j -= 1
    return reverse

#15.8
def anti_vowel(text):
    a_vowel = ''
    for i in range(len(text)):
        if text[i] not in "aeiouAEIOU":
            a_vowel += text[i]
    return a_vowel

#15.9
def scrabble_score(word):
    total = 0
    for i in word:
        j= i.lower()
        total += score[j]
    return total

#15.10
def censor(text, word):
    txt = []
    for w in text.split():
        if w == word:
            w = "*" * len(word)
            txt.append(w)
        else:
            txt.append(w)
    text = " ".join(txt)
    return text

#15.11
def count(sequence, item):
    countN = 0

    for i in range(len(sequence)):
        if sequence[i] == item:
            countN += 1

    return countN

#15.12
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

def purify(numbers):
    temp = []
    for i in range(len(numbers)):
        if is_even(numbers[i]) == True:
            temp.append(numbers[i])
    return temp

#15.13
def product(numbers):
    temp = 1
    for i in range(len(numbers)):
        temp *= numbers[i]
    return temp

#15.14
def remove_duplicates(numbers):
    temp = []

    for i in range(len(numbers)):
        if numbers[i] not in temp:
            temp.append(numbers[i])
    return temp

#15.15
def median(numbers):
    temp = sorted(numbers)
    m = 0
    i = int(len(numbers)/2)
    if i == 0:
        m = temp[i]
        return m
    if len(numbers)%2 == 0:
        m = (temp[i]+temp[i-1])/2.0
    else:
        m = temp[i]
    return m

    
