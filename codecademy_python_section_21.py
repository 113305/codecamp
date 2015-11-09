#21.1
my_file = open("output.txt", "r+")

# You can open files in write-only mode ("w"),
# read-only mode ("r"), read and write mode ("r+"),
# and append mode ("a", which adds any new data you write to the file to the end of the file).

#21.2
my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

for i in my_list:
    my_file.write(str(i) + "\n")

my_file.close()

#21.3
my_file = open("output.txt", "r")
print my_file.read()
my_file.close()

#21.4
my_file = open("output.txt", "r")
print my_file.read()
my_file.close()

#21.5
my_file = open("text.txt", "r")

print my_file.readline()
print my_file.readline()
print my_file.readline()

my_file.close()

#21.6
# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")



write_file.close()
print read_file.read()

#21.8
with open("text.txt", "w") as my_file:
    my_file.write("test")


#21.9
with open("text.txt", "w") as my_file:
    my_file.write("test")

print my_file.closed

if my_file.closed == False:
    my_file.close()
