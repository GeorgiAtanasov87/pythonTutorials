#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'safsafadssadf',
            'blog': 'Vadasdasdadasdf',
            'luggage': '123234'}

import sys

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name
