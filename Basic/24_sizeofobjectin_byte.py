"""
Created on 1/13/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to get the size of an object in bytes
"""

import sys
str1= "str1"
str2= "str2"
str3= "str3"
print()
print("Memory size of '"+str1+" = "+str(sys.getsizeof(str1))+ " bytes")
print("Memory size of '"+str2+" = "+str(sys.getsizeof(str2))+ "bytes")
print("Memory size of '"+str3+" = "+str(sys.getsizeof(str3))+ "bytes")
print()
