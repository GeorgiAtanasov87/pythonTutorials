
def mult(val):
    return val * 2

my_list = [0, 1, 2, 10, 100, 1000]

iter = map(mult, my_list)
print(type(iter))
print(iter)

print(list(iter)) #map in Python 3 returns iterator, not list!
