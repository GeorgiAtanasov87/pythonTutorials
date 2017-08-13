a = 2
b = 'Tim'

type_a = type(a)
type_b = type(b)

print (type_a)
print (type_b)
print (f"a is {type_a}")
print (f"b is {type_b}")

print ( f"is 'a' an int - {isinstance(a, int)}")
print ( f"is 'b' an str - {isinstance(b, str)}")

c = 'cbt '
n = "nuggets"

print (c)
print (n)
print (c * 5)
print (c + n )

concat  = c + n

print (f"concat is '{concat}' and is long {len(concat)} characters")


corp = 'CBT Nuggets'

print (corp[6:10])
print (corp[0:3])
print (corp[-10:-7])
print (corp[4:])

#String methods
#str.split - returns the position the searched string starts
print (f"'ugg' is in position {corp.find('ugg')} in 'corp' string")

#str.split - splits string to a list on assigned delimiter
print( corp.split(' '))

#Exersize:
print('\n\n\n Exersize:')
ui =  input("Enter a number: ")
print("The data type is originally", (type(ui)))
uconv = int(ui)
print("Now the d.t. is", (type(uconv)))
power = uconv ** 8
print(ui, "raised to the 8th power is: ", power)
