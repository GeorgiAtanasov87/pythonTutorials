for letter in 'Python':
    print('Current letter is: ', letter)

for veg in ['celery', 'mushroom', 'okra']:
    print('Current vegetable is: ', veg)

#looping tuples!!
tuplist = [(1, 2), (3, 4), (5, 6)]
for (a, b) in tuplist:
    print(a, b)


import os #for administrative automation!!
for k, v in os.environ.items():
    print(f"{k} = {v}")
