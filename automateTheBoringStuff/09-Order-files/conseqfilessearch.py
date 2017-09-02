#! python3
# bigfilessearch.py - searches directory for numbered files with a prefix
# if there are numbers missing it renames the following files

import os, shutil, re

fileRegex = re.compile(r'(Shark\.Tank\.S08E)(\d\d)(.*)')
destPath = r'H:\Movies\Shark Tank - Season 8'
# Walk all fodlers and subfolders

files = os.listdir(destPath)
#print(files)

for f in os.listdir(destPath):
    if fileRegex.search(f):
        print(fileRegex.search(f).group(2))
