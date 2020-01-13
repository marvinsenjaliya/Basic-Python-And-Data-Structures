"""
Created on 1/13/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to list all files in a directory in Python.
"""

import os, fnmatch

listOfFiles = os.listdir('.')
pattern = "*.py"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            print (entry)
            
