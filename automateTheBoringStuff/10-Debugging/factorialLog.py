#! python3

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(level=logging.DEBUG)
logging.debug('Start of program')

def factorial(n):
    logging.debug(f'Start of factorial({n})')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.warning('This is a warning!')
logging.debug('End of program')
