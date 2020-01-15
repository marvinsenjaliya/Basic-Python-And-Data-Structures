"""
Created on 1/15/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to find common items from two lists.  
"""


list1=[1,2,3,4,5]
list2=[6,2,3,9,10]
for index in list1:
	if index in list2:
		print(index)

