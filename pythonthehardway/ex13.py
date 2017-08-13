from sys import argv

# read the WYSS section for how to run this
#script, first, second, third = argv
#script, fname, lname = argv
#script, fname, mname, lname, age, gender = argv
script, fname, mname, lname = argv

#print("The script is called:", script)
#print("Your first variable is:", first)
#print("Your second variable is:", second)
#print("Your third variable is:", third)

age = input("How old are you?")
gender = input("What is your gender?")
#print("Your first name is:", fname)
#print("Your last name is:", lname)
print(f"Your name is {fname} {mname} {lname} and you are {age} years old {gender}.")
