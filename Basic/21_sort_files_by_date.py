"""
Created on 1/13/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
write a python program to sort three number without using conditional statement:
"""

import glob
import os

files = glob.glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))
 
