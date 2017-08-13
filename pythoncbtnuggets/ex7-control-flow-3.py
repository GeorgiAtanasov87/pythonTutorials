#!/usr/bin/python

yn = input("Contrinue? Yes or No: ")
yn = yn.lower()

if yn[0] == 'y':
    print("You typed 'Yes.'")
elif yn[0] == 'n':
    print("You typed 'No'")
elif yn == 'spam':
    print("What are you doing?!")
else:
    print("You entered an invalid response.")
