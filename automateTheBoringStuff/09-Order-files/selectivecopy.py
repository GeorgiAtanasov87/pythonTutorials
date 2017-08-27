#! python3
# selectivecopy.py - walks a folder and all its subfolders and copies all
# files with certain extension to destination folder
# inputs:
#   sourcePath - path to folder to be walked
#   destPath - path to folder to be walked
#   ext - extension of files to be copied


import os, shutil, re

fileExtRegex = re.compile(r'(.+)(\.pdf)$')
sourcePath = r'C:\Users\Joro\Documents\GitHub\pythonTutorials\automateTheBoringStuff'
destPath = r'C:\Users\Joro\Desktop\pythontests'
# Walk all fodlers and subfolders
for root, dirs, files in os.walk(sourcePath):
    for fileName in files:
        if fileExtRegex.search(fileName):
            #print (fileName)
            fullPath = os.path.join(root, fileName)
            #print(fullPath)
            newAbsPath = os.path.join(destPath, fileName)
            shutil.copy(fullPath, newAbsPath)
        #print (sFile)
