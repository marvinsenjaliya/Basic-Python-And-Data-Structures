"""
Created on 1/13/2020
@author:Marvin Senjaliya
"""


"""
problem statement:
Write a Python program to find files and skip directories of a given directory.
"""

import os
print([f for f in os.list.dir('C:\Users\Marvin 
Senjaliya\Desktop\Basic-Python-And-Data-Structures\Basic) 
if os.path.isfile(os.path.join('C:\Users\Marvin 
Senjaliya\Desktop\Basic-Python-And-Data-Structures\Basic',f))])
