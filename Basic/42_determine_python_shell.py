"""
Created on 1/13/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on 
operating system. 
"""

import struct
print(struct.calcsize("p",8))

