"""
Created on 1/13/2020
@author:Marvin Senjaliya
"""


"""
problem statement:
Write a Python program to remove the first occurrence of a specified element from an array. 
"""

import array as arr
a=arr.array('i',[1,2,3,4,5])
a.remove(a[0])
print(a)
