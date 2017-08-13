from sys import argv

script, filename = argv

print(f"We're going to erease {filename}.")
print("If you don't want that, hit CTRl-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Openning the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Now I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")

print("The content of the file is: ")
target.close()

file_read = open(filename, 'r')
print(file_read.read())
file_read.close()
