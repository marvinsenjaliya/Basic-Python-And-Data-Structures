"""
Created on 1/13/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
Write a python program to access environment variables.
"""
#import os liberary
import os
#Access all environment variables
print(os.environ)
# Access a particular environment variable 
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*') 
