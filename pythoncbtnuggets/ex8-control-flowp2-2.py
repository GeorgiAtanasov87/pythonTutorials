f = open('E:/Git/pythoncbtnuggets/ex8-test.txt')
for line in f:
    print(line)

print('\n' * 3) # new example

nm = {'Key 1': 'Value 1', 'Key 2':'Value 2'}
for k, v in nm.items():
    print(k,v)

print('\n' * 3) # new example

i = ["abc", 123, (5, 6), 4.20]
query = [(5, 6), 3.14]
for key in query:
    if key in i:
        print(key, "was found")
    else:
        print(key, "not found!")

print('\n' * 3) # new example

for mult in range(4,7): # Runs 3 iterations, 4, 5 and 6
    for i in range(1, 11): # Going to print a single mult ..
        print(i, 'x', mult, '=', i * mult)
    print()
