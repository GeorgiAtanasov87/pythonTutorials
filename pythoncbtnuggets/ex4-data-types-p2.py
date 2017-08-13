#Tuples
    #Def1: an ordered set of data
    #Def2: a single row in a DB table
    #Tuples are immutable
    #good for static program data (constants)

atuple = ('perl', 'ruby', 'python', '3.14', 4000)

#clears the screen in interactive shell
def wiper():
    print("\n" * 100)

#wiper()

newtup = (1, "sometext", 3.14)
print( type(newtup) )
print( len(newtup) )
print( type(newtup[1]) )

newtup2 = newtup[0:2]
print( newtup2)
print( newtup2.index('sometext'))


multitup = ("tim", 12, "tim", 24.234)
print(f"multitup is: {multitup}")
print(f"Count of 'tim' in multitup is {multitup.count('tim')}")

#list - mutable sequence data structure
print("\n\n\nLists: a mutable sequence data structure")
alist = ["Sales", 25, "Admin", 1.0]
print(f"example of a list: {alist}")
print( type(alist) )

foo = ["spam", 335, "eggs", 323.234]
foo2 = foo[0:3]
print(foo2)
foo2.remove(335)
print(foo2)
footup = tuple(foo2)
print(footup)
print(type(footup) )

foo2.append(3.14)
print(foo2)

foo2.insert(1, "foo")
print(foo2 )
foo2.insert(3, "bar")
foo2.reverse()
print(foo2)

foo2[0] = str(foo2[0])
foo2.sort()
print(foo2)


#Dictionaries - mutable unordered set of key:value pairs (assoc. array, hash tables)
print('\n\n\nDictionaries - mutable unordered set of key:value pairs (assoc. array, hash tables)')
adict = {'one':'uno', 'two':'dos', 'three':'tres'}

months = {1: 'January', 2: "February", 3: "March"}
print(months)
print(type(months))
months[4] = "April"
print(months)
print(months.keys())
print(months.values())
months[4] = "Something else"
print(months)

month2list = list(months)
print(month2list) #converted the dict keys to a list
month2list2 = list(months.values()) #converted the dict values to a list
print(month2list2)

#Nesting
print("Nesting a tuple in a dict:")
tup = ("some", "data", "here")
months[4] = tup
print(months)

print("Nesting a dict in a dict:")
l1 = ["one", "two", "three", "four"]
l2 = [1, 2, 3, 4]
l1.append(l2)
print(l1)

print(adict)
print(len(adict))
adict.pop('three')
print(adict)


print('\n\n\n\n\n\nExample:')

val1 = input("Enter str element 1/3: ")
val2 = int(input("Enter int element 2/3: "))
val3 = float(input("Enter float element 3/3: "))

lst = [val1, val2, val3]
tpl = (val1, val2, val3)
dict = {"First element: ":val1, "Second element: ":val2, "Third element: ": val3}

print('\n')
print("Here is yuour list: ", lst)
print("Here is your tuple: ", tpl)
print("Here is your dictionary: ", dict)

print('\n')
val4 = input("Add a new str list element: ")
lst.append(val4)
print("Here is your new list: ", lst)
