import random, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(level=logging.DEBUG)
guess = ''
while guess not in ('heads', 'tails'):
    toss = random.randint(0,1) # 0 is tails, 1 i s heads
    logging.debug(f'toss is {toss}')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
if guess == 'heads':
    guess = 1
else:
    guess = 0

logging.debug(f'Toss is {toss} and Guess is {guess}')
if toss == guess:
    print('You got it')
else:
    print('Nope!, Guess again!')

    toss2 = random.randint(0,1) # 0 is tails, 1 i s heads
    logging.debug(f'Toss2 is {toss2}')
    guess2 = input()
    logging.debug(f'Toss is {toss} and Guess is {guess}')

    if guess2 == 'heads':
        guess2 = 1
    else:
        guess2 = 0
    if toss2 == guess2:
        print('You got it !')
    else:
        print('Nope. You are really bad at this game.')
