#! python3
# passStrength.py - script checking the strength of a password

import re, sys

password = input('Enter password: ')

passRegex = re.compile(r'''(
    (.{8,})         # at least 8 char long
    ([A-Z]+)        # has uppercase char
    ([a-z]+)        # has lowercase char
    )''', re.VERBOSE)

lenRegex = re.compile(r'(.{8,})')
if lenRegex.search(password) == None:
    sys.exit('Error!\nPass must be at least 8 chars long.')

ucRegex = re.compile(r'([A-Z]+)')
if ucRegex.search(password) == None:
    sys.exit('Error!\nPass must contain Uppercase char.')

lcRegex = re.compile(r'([a-z]+)')
if lcRegex.search(password) == None:
    sys.exit('Error!\nPass must contain Lowercase char.')

dRegex = re.compile(r'([0-9]+)')
if dRegex.search(password) == None:
    sys.exit('Error!\nPass must contain a digit.')

print('Pass is Good')
