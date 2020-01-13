"""
Created on 1/13/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to get an absolute file path
"""

#define the function 
def absolute_file_path(path_fname):
	import os
	return os.path.abspath('path_fname')
#print the absolute path of file
print("Absolute file path: ",absolute_file_path("18_absolute_file_path.py)
