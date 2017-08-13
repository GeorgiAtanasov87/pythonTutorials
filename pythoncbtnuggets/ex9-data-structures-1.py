s1 = set([0, 2, 4, 6])
print('s1 is a set: ', s1)
s2 = set('cbtnuggets')
s3 = set([10, 12, 14, 16])

print('s3 is a set: ', s3)
print('s1.update(s3) updates s1 to: ')
s1.update(s3)
print(s1)

newset = set(s1) #new object with diferent place in the pc memory
print('newset is: ', newset)
print(id(s1)) #id gives the location in the memory of s1
print(id(newset)) #id gives the location in the memory of s3

sx = s1 #both will have the same id (place in pc memory)
print(id(s1))
print(id(sx))
