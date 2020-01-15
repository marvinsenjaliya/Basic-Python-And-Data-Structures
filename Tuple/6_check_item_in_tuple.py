"""
Created on 1/15/2020
@author :Marvin Senjaliya
"""


"""
problem statement:
Write a Python program to check whether an element exists within a tuple
"""

tuple=(1,2,3,4,5)
list=list(tuple)
num = 2
for i in list:
	if num==i:
		print("yes,present")

