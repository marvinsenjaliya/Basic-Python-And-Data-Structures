"""
Created on 1/14/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to count number of items in a dictionary value that is a list. 
"""


#take input as a dictionary
dictionary={'int':[1,2,3],'float':[2.0,3.33,9.6]}
#use for loop and take type of value 
for value in dictionary.values():
	if type(value)==list:
		print(value)
