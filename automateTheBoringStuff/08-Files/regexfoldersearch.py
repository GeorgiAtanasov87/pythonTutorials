#! python3
# regexfoldersearch.py - iterates over all files in a folder for regex
# matches and displays the reulsts.

import re, os, pprint

# print(os.listdir())
varRegex = re.compile('(Hello )(\D{5})')
results = {}
for sFile in os.listdir():
    #print(sFile)
    if os.path.isfile(sFile):
        results[sFile] = []
        fobj = open(sFile, 'r')
        for line in fobj:
            if varRegex.search(line):
                res = varRegex.search(line)
                #print(res[2])
                results[sFile].append(res[2])
        fobj.close()
pprint.pprint(results)
