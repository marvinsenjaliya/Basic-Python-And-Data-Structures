"""
Created on 1/13/2020
@author :Marvin Senjaliya
"""

"""
problem statement 
Write a Python program to get file creation and modification date/times
"""

#import time library
import os.path,time
#print the modification time 
print("print last modified: %s"time.ctime(os.path.getmtime("19_creation_modification_time.py")))
#print the creation time 
print("print last modified: %s"time.ctime(os.path.getctime("19_creation_modification_time.py")))
