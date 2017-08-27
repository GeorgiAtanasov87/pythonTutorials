#! python3
# madlibs.py - script replacing words 'ADJECTIVE', 'NOUN', 'VERB'

import re

adjRegex = re.compile('ADJECTIVE')
vbRegex = re.compile('VERB')
nnRegex = re.compile('NOUN')

adj = str(input('Enter replacement ADJECTIVE: '))
vb = str(input('Enter replacement VERB: '))
nn = str(input('Enter replacement NOUN: '))

resFile = open('madlib_result.txt', 'w')
sfile = open('sample_text.txt', 'r')
for line in sfile:
    l1 = adjRegex.sub(adj, line)
    l2 = vbRegex.sub(vb, l1)
    l3 = nnRegex.sub(nn, l2)
    resFile.write(l3 + '\n')
    print (l3)

sfile.close()
resFile.close()
