# While loop examples:

x = 0
y = 13

while x < y:
    print(x)
    x += 1

print('\n' * 3)# another example

a = 0
while a < 13:
    a +=1
    if a ==5:
        continue
    if a == 10:
        break
    print(a)
