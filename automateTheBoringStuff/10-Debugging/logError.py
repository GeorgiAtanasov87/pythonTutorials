#! python3
# logError.py - raises an exception and loggs the error to file.

import traceback
try:
	raise Exception('This is the error message.')
except:
	errorFile = open(r'C:\Users\Joro\Documents\GitHub\pythonTutorials\automateTheBoringStuff\10-Debugging\errorInfo.txt', 'w')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback ifo was written to errorInfo.txt')
