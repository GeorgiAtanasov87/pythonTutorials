#! python3
# bigfilessearch.py - searches directory and subdirs for large files (>100Mb)
# inputs:
#   fullPath - path to searched directory
# outputs:
#   prints all files bigger than 100Mb

import os, shutil, re

sourcePath = r'E:\\'
# Walk all fodlers and subfolders
for root, dirs, files in os.walk(sourcePath):
    for fileName in files:
        fullPath = os.path.join(root, fileName)
        if os.path.getsize(fullPath) > (10 ** 8):
            print( fileName, 'Size: ', os.path.getsize(fullPath))
        #if fileExtRegex.search(fileName):
            #print (fileName)
        #    fullPath = os.path.join(root, fileName)
            #print(fullPath)
