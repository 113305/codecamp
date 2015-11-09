#18.3
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

#18.4
for i in range(2,6):
    print bin(i)

#18.5
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001",2)

#18.6
shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)

#18.7
print bin(0b1110 & 0b101)

#18.8
print bin(0b1110 | 0b101)

#18.9
print bin(0b1110 ^ 0b101)

#18.11
def check_bit4(input):
    mask = 0b1000
    if input & mask > 0:
        return "on"
    else:
        return "off"

#18.12
a = 0b10111011
mask = 0b100
desired = a | mask
print bin(desired)

#18.13
a = 0b11101110
mask = 0b11111111

print bin(a ^ mask)

#18.14
def flip_bit(number, n):
    mask = (0b1 << n-1)
    result = number ^ mask
    return bin(result)
