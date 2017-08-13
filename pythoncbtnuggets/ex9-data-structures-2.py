#sets examples:

lang = ['lisp', 'python', 'abc', 'c', 'python', 'ruby', 'perl', 'ruby']
print('list lang is: ', lang)
l1 = set(lang)
print(lang)
print('l1 = "set(lang)" is : ', l1) # the dublicates from lang are gone!!!

morelang = ['sql', 'erlang', 'perl', 'haskell']
l2 = set(morelang)
print(l2)

print(l1 - l2) #the members of l1 except those in l2

print(l1.intersection(l2)) # gives the common members of the 2 sets


#set comprehension
s1 = set([0, 2 ,4 ,6])
s2 = set([10, 12, 14, 16])

setcomp = {i * 2 for i in s2} #multiplies each momber of s2 by 2
print('s2 = ', s2)
print('setcomp = ', setcomp)

#list comprehension
alist = [1, 2, 4, 6, 8, 10]
alist = [i * 4 for i in alist]
print(alist)

phrase = 'Lorem ipsum dolor sit amet, consectetur \
adipiscing elit. Duis commodo aliquet feugiat. \
Aliquam eget luctus ex, at dignissim est.'.split()
print(type(phrase))
print(phrase)

stuff = [[p.upper(), p.lower(), len(p)] for p in phrase]
print(stuff)

#dictionary comprehension
print('\n' * 3)
dic1 = {'ay':1, 'bee':2, 'cee':3}
print(dic1)
dic2 = {value:key for key, value in dic1.items()}
print(dic2)

lang =list(open('E:/Git/pythoncbtnuggets/ex9-lang.txt'))
print(lang)
lang = [n.rstrip() for n in lang]
print(lang)
