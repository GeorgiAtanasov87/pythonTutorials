from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

filename_from_input = input("Please enter your filename: ")

txt_input = open(filename_from_input)
print(txt_input.read())
